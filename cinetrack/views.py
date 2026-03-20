from collections import defaultdict
from urllib.parse import unquote
import re, unicodedata

from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Case, Count, IntegerField, When, Q
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from rest_framework import viewsets

from .forms import ContenidoForm, SagaAliasForm, MaratonForm
from .models import Contenido, SagaAlias, Maraton
from .serializers import ContenidoSerializer
from .utils import buscar_contenido_tmdb


CALIF_MAP = {
    'excelente': 5,
    'buena': 4,
    'regular': 3,
    'mala': 2,
    'horrible': 1,
}


def clave_saga_desde_titulo(titulo: str) -> str:
    """
    Genera una clave corta de saga a partir del título.
    Ejemplos: "harry potter", "star wars", "jurassic", etc.
    """
    if not titulo:
        return ""

    # 1) Quitar acentos y pasar a minúsculas
    def quitar_acentos(texto: str) -> str:
        texto_normal = unicodedata.normalize("NFD", texto)
        return "".join(ch for ch in texto_normal if not unicodedata.combining(ch))

    texto = quitar_acentos(titulo).lower().strip()

    # 2) Cortar subtítulos (antes de :, -, –, —, (, [)
    parte_principal = re.split(r'[:\-\u2013\u2014\(\[]', texto, maxsplit=1)[0].strip()

    # 3) Separar en palabras (solo letras y números)
    palabras = re.findall(r"[a-z0-9]+", parte_principal, flags=re.I)
    if not palabras:
        return ""

    # 4) Quitar artículos iniciales (español/inglés)
    ARTICULOS = {
        "el", "la", "los", "las", "un", "una", "uno", "unos", "unas",
        "the", "a", "an", "otro", "otra", "otros", "otras",
    }
    while palabras and palabras[0] in ARTICULOS:
        palabras.pop(0)
    if not palabras:
        return ""

    # Franquicias de 1 palabra (clave directa)
    FRANQUICIAS_1P = {"shrek"}  # ← aquí
    if palabras and palabras[0] in FRANQUICIAS_1P:
        return palabras[0]

    # 5) Franquicias conocidas (2 palabras)
    FRANQUICIAS = {
        "harry potter", "star wars", "señor anillos", "el señor",
        "jurassic park", "jurassic world", "toy story",
        "rapidos furiosos", "rapido furioso", "mision imposible",
        "piratas caribe", "guardianes galaxia", "spider man", "spiderman",
    }
    if len(palabras) >= 2 and (" ".join(palabras[:2]) in FRANQUICIAS):
        return " ".join(palabras[:2])

    # 6) Limpiar sufijos: parte/temporada/season + número, números, romanos
    ROMANOS = {"i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"}

    base = " ".join(palabras)
    base = re.sub(r"(?:parte|part|temporada|season)\s*\d+$", "", base).strip()
    base = re.sub(r"\d+$", "", base).strip()

    palabras_limpias = base.split()
    if palabras_limpias and palabras_limpias[-1] in ROMANOS:
        palabras_limpias.pop()

    # 7) Regla final
    if len(palabras) >= 2:
        if palabras[1].isdigit() or palabras[1] in ROMANOS:
            return palabras[0]
        return " ".join(palabras[:2])

    return palabras[0]


def nombre_saga_visible(clave: str, fallback: str) -> str:
    alias = SagaAlias.objects.filter(key=clave).first()
    return alias.nombre if alias else fallback


def home(request):
    DONUT_CIRCUNFERENCIA = 326
    MAXIMO_POR_PLATAFORMA = 5

    # 1) Pósters para los rollos (aleatorios)
    posters_rollo = (
        Contenido.objects
        .exclude(imagen__isnull=True, imagen__exact='')
        .order_by('?')[:64]
    )

    # 2) Conteos globales
    qs_contenidos = Contenido.objects.all()
    total = qs_contenidos.count()
    peliculas = qs_contenidos.filter(tipo='pelicula').count()
    series = qs_contenidos.filter(tipo='serie').count()
    vistos = qs_contenidos.filter(estado='vista').count()
    pendientes = qs_contenidos.filter(estado='pendiente').count()
    favoritas = qs_contenidos.filter(favorita=True).count()

    # 3) Promedio de calificación (string → número con CALIF_MAP)
    calificaciones = list(
        qs_contenidos.exclude(calificacion__isnull=True, calificacion__exact='')
                     .values_list('calificacion', flat=True)
    )
    calificaciones_numeros = [CALIF_MAP[c] for c in calificaciones if c in CALIF_MAP]
    promedio = round(sum(calificaciones_numeros) / len(calificaciones_numeros), 1) if calificaciones_numeros else 0.0
    calificados = len(calificaciones_numeros)

    # 4) Donut del promedio
    porcentaje_promedio = (promedio / 5.0) * 100 if promedio else 0
    desplazamiento_donut = round(DONUT_CIRCUNFERENCIA * (1 - porcentaje_promedio / 100), 2)

    # 5) Barras por plataforma (top 5)
    mapa_plataformas = dict(Contenido.PLATAFORMAS)
    conteos_plataforma = (
        qs_contenidos.exclude(plataforma__isnull=True, plataforma__exact='')
                     .values('plataforma')
                     .annotate(n=Count('id'))
                     .order_by('-n')[:5]
    )
    barras_plataforma = []
    for fila in conteos_plataforma:
        nombre = mapa_plataformas.get(fila['plataforma'], fila['plataforma'])
        cantidad = fila['n']
        porcentaje_barra = int(round((cantidad / total) * 100)) if total else 0
        barras_plataforma.append({'nombre': nombre, 'cantidad': cantidad, 'porcentaje': porcentaje_barra})

    porcentaje_completado = int(round((vistos / total) * 100)) if total else 0

    estadisticas = {
        'total': total,
        'peliculas': peliculas,
        'series': series,
        'vistos': vistos,
        'pendientes': pendientes,
        'promedio': promedio,
        'calificados': calificados,
        'favoritas': favoritas,
    }

    # 6) Actividad reciente (últimos con imagen)
    actividad_reciente = (
        Contenido.objects
        .exclude(imagen__isnull=True, imagen__exact='')
        .order_by('-updated_at', '-created_at')[:12]
    )

    # 7) Top 5 por calificación (mapea a número para ordenar)
    top_calificados = (
        Contenido.objects
        .exclude(imagen__isnull=True, imagen__exact='')
        .exclude(calificacion__isnull=True, calificacion__exact='')
        .annotate(
            calificacion_num=Case(
                When(calificacion='excelente', then=5),
                When(calificacion='buena', then=4),
                When(calificacion='regular', then=3),
                When(calificacion='mala', then=2),
                When(calificacion='horrible', then=1),
                default=0,
                output_field=IntegerField(),
            )
        )
        .order_by('-calificacion_num', '-updated_at', '-created_at')[:5]
    )

    # 8) Lo más visto por plataforma (máx 5 por plataforma)
    plataformas_ordenadas = sorted(Contenido.PLATAFORMAS, key=lambda p: p[1].lower())
    tops_plataformas = []
    for codigo, nombre in plataformas_ordenadas:
        items = (
            Contenido.objects
            .filter(plataforma=codigo, estado='vista')
            .exclude(imagen__isnull=True, imagen__exact='')
            .order_by('-veces_vista', '-updated_at', '-created_at')[:MAXIMO_POR_PLATAFORMA]
        )
        if items:
            tops_plataformas.append({'codigo': codigo, 'nombre': nombre, 'items': items})

    return render(request, 'cinetrack/home.html', {
        'contenidos': posters_rollo,
        'estadisticas': estadisticas,
        'barras_plataforma': barras_plataforma,
        'porcentaje_completado': porcentaje_completado,
        'desplazamiento_donut': desplazamiento_donut,
        'actividad_reciente': actividad_reciente,
        'top_calificados': top_calificados,
        'tops_plataformas': tops_plataformas,
    })


def catalogo(request):
    contenidos = Contenido.objects.all()

    # Parámetros
    tipo = request.GET.get('tipo') or ''
    plataforma = request.GET.get('plataforma') or ''
    estado = request.GET.get('estado') or ''
    favorita = request.GET.get('favorita')
    volveria = request.GET.get('volveria_a_ver')

    # Filtros (aplica "volvería a ver" primero)
    if volveria in ('1', 'true', 'True', 'on'):
        contenidos = contenidos.filter(volveria_a_ver=True, estado='vista')
    if tipo:
        contenidos = contenidos.filter(tipo=tipo)
    if plataforma:
        contenidos = contenidos.filter(plataforma=plataforma)
    if estado:
        contenidos = contenidos.filter(estado=estado)
    if favorita == '1':
        contenidos = contenidos.filter(favorita=True)

    contenidos = contenidos.order_by('titulo')

    # Plataformas (chips)
    plataformas_disponibles = sorted(Contenido.PLATAFORMAS, key=lambda p: p[1].lower())
    plataforma_nombre = dict(plataformas_disponibles).get(plataforma)

    # Buscador
    buscar = (request.GET.get("buscar") or "").strip()
    if buscar:
        contenidos = contenidos.filter(Q(titulo__icontains=buscar))

    # Agrupar por saga
    cubetas = defaultdict(list)
    for item in contenidos:
        cubetas[clave_saga_desde_titulo(item.titulo)].append(item)

    grupos = []
    for clave in sorted(cubetas.keys()):
        items = cubetas[clave]
        if len(items) >= 2:
            def orden_grupo(x):
                anio = x.fecha.year if getattr(x, 'fecha', None) else 9999
                return (not bool(getattr(x, 'tendra_continuacion', False)), anio, x.titulo.lower())

            items_ordenados = sorted(items, key=orden_grupo)
            representativo = items_ordenados[0]
            base = representativo.titulo.split(':')[0].split('-')[0].strip()
            nombre_visible = nombre_saga_visible(clave, base)
            grupos.append({
                'saga': nombre_visible,
                'items': items_ordenados,
                'count': len(items_ordenados),
                'grouped': True,
                'key': clave,
            })
        else:
            for it in items:
                grupos.append({
                    'saga': it.titulo,
                    'items': [it],
                    'count': 1,
                    'grouped': False,
                })

    # Orden alfabético por nombre visible del grupo
    grupos.sort(key=lambda g: g['saga'].lower())

    # Paginación
    paginador = Paginator(grupos, 24)
    page_obj = paginador.get_page(request.GET.get("page"))
    pagina = page_obj.number  # ← usa el número real de la página

    return render(request, "cinetrack/catalogo.html", {
        "buscar": buscar,
        "pagina": pagina,
        "page_obj": page_obj,
        "page_groups": page_obj,
        "plataformas": plataformas_disponibles,
        "plataforma_nombre": plataforma_nombre,
        "filtros": {
            "tipo": tipo,
            "plataforma": plataforma,
            "estado": estado,
            "favorita": favorita,
            "volveria_a_ver": volveria,
            "buscar": buscar,
        },
        "saga_form": SagaAliasForm(),
    })


def detalle(request, pk):
    contenido = get_object_or_404(Contenido, pk=pk)
    clave_saga = clave_saga_desde_titulo(contenido.titulo)
    origen = request.GET.get("origen") or "catalogo"
    pagina = request.GET.get("page")

    # Pertenece a un grupo si hay >1 con la misma clave de saga
    titulos = (
        Contenido.objects
        .exclude(titulo__isnull=True)
        .values_list("titulo", flat=True)
    )
    en_grupo = sum(1 for t in titulos if clave_saga_desde_titulo(t) == clave_saga) > 1

    return render(request, "cinetrack/detalle.html", {
        "contenido": contenido,
        "en_grupo": en_grupo,
        "clave_saga": clave_saga if en_grupo else None,
        "origen": origen,
        "page": pagina,
    })


def registrar(request):
    error = None

    if request.method == "POST":
        formulario = ContenidoForm(request.POST)

        if formulario.is_valid():
            titulo = formulario.cleaned_data["titulo"]
            plataforma = formulario.cleaned_data["plataforma"]

            if Contenido.objects.filter(titulo=titulo, plataforma=plataforma).exists():
                error = "Este contenido ya fue registrado previamente."
            else:
                formulario.save()
                return redirect("cinetrack:catalogo")
    else:
        formulario = ContenidoForm()

    return render(request, "cinetrack/registrar.html", {
        "formulario": formulario,
        "error": error,
    })


def editar(request, pk):
    contenido = get_object_or_404(Contenido, pk=pk)

    clave_saga = clave_saga_desde_titulo(contenido.titulo)
    titulos = (
        Contenido.objects
        .exclude(titulo__isnull=True)
        .values_list("titulo", flat=True)
    )
    en_grupo = sum(1 for t in titulos if clave_saga_desde_titulo(t) == clave_saga) > 1

    pagina = request.GET.get("page")  # captura la página

    if request.method == "POST":
        formulario = ContenidoForm(request.POST, instance=contenido)
        if formulario.is_valid():
            formulario.save()
            if pagina:
                return redirect(f"{reverse('cinetrack:catalogo')}?page={pagina}")
            return redirect("cinetrack:detalle", pk=contenido.pk)
    else:
        formulario = ContenidoForm(instance=contenido)

    return render(request, "cinetrack/editar.html", {
        "contenido": contenido,
        "formulario": formulario,
        "en_grupo": en_grupo,
        "clave_saga": clave_saga if en_grupo else None,
        "page": pagina,
    })


def eliminar(request, pk):
    contenido = get_object_or_404(Contenido, pk=pk)

    if request.method == "POST":
        titulo = contenido.titulo
        contenido.delete()

        # Si es AJAX, respondemos JSON (sin redirect)
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({
                "ok": True,
                "id_eliminado": pk,
                "titulo": titulo
            })

        messages.success(request, f"🗑️ '{escape(titulo)}' fue eliminado correctamente.")
        return redirect("cinetrack:catalogo")

    # No POST
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse({"ok": False, "error": "Método no permitido"}, status=405)

    return redirect("cinetrack:catalogo")


def buscar(request):
    resultados = []
    error = None

    # 1) Si hay búsqueda (POST) intenta consultar TMDb
    if request.method == "POST":
        query = (request.POST.get("query") or "").strip()
        if query:
            try:
                resultados = buscar_contenido_tmdb(query)
            except Exception:
                # No exponemos detalles de error al usuario; mantenemos limpio el UI
                error = "No se pudo obtener resultados en este momento."
        else:
            error = "Escribe un título para buscar."

    # 2) Preparar lista de plataformas (orden alfabético) dejando 'otro' al final
    opciones = list(Contenido.PLATAFORMAS)
    otras = [p for p in opciones if p[0] == "otro"]
    normales = sorted((p for p in opciones if p[0] != "otro"), key=lambda p: p[1].lower())
    plataformas_ordenadas = normales + otras  # 'Otra' hasta el final

    return render(request, "cinetrack/buscar.html", {
        "resultados": resultados,
        "plataformas": plataformas_ordenadas,
        "error": error,
    })


@csrf_exempt
def guardar_desde_busqueda(request):
    if request.method == "POST":
        # Datos obligatorios
        titulo = request.POST.get("titulo")
        plataforma = request.POST.get("plataforma")

        if not titulo or not plataforma:
            messages.error(request, "Faltan datos para guardar el contenido.")
            return redirect("cinetrack:buscar")

        # Verificación de duplicados por título + plataforma
        if Contenido.objects.filter(titulo=titulo, plataforma=plataforma).exists():
            messages.warning(request, f"⚠️ '{escape(titulo)}' ya existe en tu lista.")
            return redirect("cinetrack:buscar")

        # Crear registro
        Contenido.objects.create(
            titulo=titulo,
            resumen=request.POST.get("resumen"),
            fecha=request.POST.get("fecha") or None,
            imagen=request.POST.get("imagen"),
            tipo=request.POST.get("tipo"),
            plataforma=plataforma,
            calificacion=request.POST.get("calificacion") or None,
            veces_vista=request.POST.get("veces_vista") or 0,
            volveria_a_ver=bool(request.POST.get("volveria_a_ver")),
            estado=request.POST.get("estado"),
            tendra_continuacion=request.POST.get("tendra_continuacion") == "on",
            favorita=request.POST.get("favorita") == "on",
        )

        messages.success(request, f"✅ '{escape(titulo)}' fue registrada exitosamente.")
        return redirect("cinetrack:buscar")

    # Si no es POST
    return redirect("cinetrack:buscar")


def pendientes(request):
    # Construir columnas Kanban (solo estado=pendiente), usando las fases del modelo
    ICONOS_FASE = {
        "nuevo": "bi-lightning",
        "pronto": "bi-clock",
        "encurso": "bi-play-circle",
        "pausado": "bi-pause-circle",
    }

    fases = []
    for codigo, etiqueta in Contenido.FASES_KANBAN:
        qs = (Contenido.objects
              .filter(estado="pendiente", fase_kanban=codigo)
              .order_by("-updated_at", "titulo"))
        fases.append((codigo, etiqueta, ICONOS_FASE.get(codigo, ""), qs))

    return render(request, "cinetrack/pendientes.html", {"fases": fases})


@require_POST
def mover_fase(request, pk):
    item = get_object_or_404(Contenido, pk=pk)
    fase = request.POST.get("fase")

    fases_validas = {c for c, _ in Contenido.FASES_KANBAN}
    if fase not in fases_validas:
        return JsonResponse({"ok": False, "error": "Fase inválida"}, status=400)

    item.fase_kanban = fase
    item.save(update_fields=["fase_kanban", "updated_at"])
    return JsonResponse({"ok": True, "id": item.pk, "fase": item.fase_kanban})


@require_POST
def marcar_vista(request, pk):
    item = get_object_or_404(Contenido, pk=pk)
    item.estado = "vista"
    item.save(update_fields=["estado", "updated_at"])
    return redirect("cinetrack:pendientes")


def favoritos(request):
    # Query base: todos los marcados como favoritos
    favoritos_qs = Contenido.objects.filter(favorita=True)

    # Top 3 aleatorio (mezclado películas + series)
    top3 = list(favoritos_qs.order_by("?")[:3])

    # Listas separadas
    peliculas = favoritos_qs.filter(tipo="pelicula").order_by("-id")[:20]
    series = favoritos_qs.filter(tipo="serie").order_by("-id")[:20]

    return render(request, "cinetrack/favoritos.html", {
        "top3": top3,
        "peliculas": peliculas,
        "series": series,
    })


@require_POST
def toggle_favorita(request, pk):
    contenido = get_object_or_404(Contenido, pk=pk)
    contenido.favorita = not bool(contenido.favorita)
    contenido.save(update_fields=["favorita", "updated_at"])
    return redirect("cinetrack:favoritos")


def grupo_saga(request, clave: str):
    clave_norm = unquote(unquote(clave))
    page = request.GET.get("page")

    # Renombrar saga (POST)
    if request.method == "POST":
        nombre = (request.POST.get("nombre") or "").strip()
        if len(nombre) < 3:
            messages.error(request, "El nombre de la saga es demasiado corto (mínimo 3 caracteres).")
        else:
            SagaAlias.objects.update_or_create(key=clave_norm, defaults={"nombre": nombre})
            messages.success(request, f"Nombre de la saga actualizado a “{nombre}”.")
        return redirect(f"{request.path}?page={page}" if page else request.path)

    # GET: construir grupo
    contenidos = Contenido.objects.all().order_by("titulo")
    items = [c for c in contenidos if clave_saga_desde_titulo(c.titulo) == clave_norm]
    if not items:
        raise Http404("Grupo no encontrado")

    def orden(x):
        anio = x.fecha.year if getattr(x, "fecha", None) else 9999
        return (not bool(getattr(x, "tendra_continuacion", False)), anio, x.titulo.lower())

    items_ordenados = sorted(items, key=orden)

    base = items_ordenados[0].titulo.split(":")[0].split("-")[0].strip()
    alias = SagaAlias.objects.filter(key=clave_norm).first()
    nombre_visible = alias.nombre if alias else base

    return render(request, "cinetrack/grupo.html", {
        "saga": nombre_visible,
        "items": items_ordenados,
        "clave": clave_norm,
        "cantidad": len(items_ordenados),
        "page": page,
    })


def renombrar_saga(request):
    form = SagaAliasForm(request.POST)
    if form.is_valid():
        obj, _created = SagaAlias.objects.update_or_create(
            key=form.cleaned_data['key'],
            defaults={'nombre': form.cleaned_data['nombre'].strip() or form.cleaned_data['key']}
        )
        messages.success(request, f"✅ Saga renombrada a “{escape(obj.nombre)}”.")
    else:
        messages.error(request, "No se pudo guardar el nombre de la saga.")

    # Regresar a donde venía el usuario
    next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or '/cinetrack/catalogo/'
    return redirect(next_url)


def volverias(request):
    # Listas separadas para películas y series marcadas como "volvería a ver"
    peliculas = Contenido.objects.filter(volveria_a_ver=True, tipo="pelicula").order_by("-id")[:14]
    series = Contenido.objects.filter(volveria_a_ver=True, tipo="serie").order_by("-id")[:14]

    return render(request, "cinetrack/volveria.html", {
        "peliculas": peliculas,
        "series": series,
    })


def maratones(request):
    lista = Maraton.objects.all().order_by("-created_at")
    return render(request, "cinetrack/maratones.html", {"maratones": lista})


def detalle_maraton(request, pk):
    maraton = get_object_or_404(Maraton, pk=pk)
    items = maraton.contenidos.order_by('titulo')
    return render(
        request,
        'cinetrack/maraton_detalle.html',
        {'maraton': maraton, 'items': items}
    )


def crear_maraton(request):
    if request.method == 'POST':
        form = MaratonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Maratón creado correctamente.')
            return redirect('cinetrack:maratones')
    else:
        list(messages.get_messages(request))
        form = MaratonForm()
    return render(request, 'cinetrack/maraton_form.html', {'form': form})


def editar_maraton(request, pk):
    maraton = get_object_or_404(Maraton, pk=pk)
    if request.method == 'POST':
        form = MaratonForm(request.POST, instance=maraton)
        if form.is_valid():
            form.save()
            messages.success(request, 'Maratón actualizado.')
            return redirect('cinetrack:maratones')
    else:
        list(messages.get_messages(request))
        form = MaratonForm(instance=maraton)
    return render(request, 'cinetrack/maraton_form.html', {'form': form, 'maraton': maraton})


def eliminar_maraton(request, pk):
    maraton = get_object_or_404(Maraton, pk=pk)
    if request.method == "POST":
        nombre = maraton.nombre
        maraton.delete()
        messages.success(request, f"🗑️ Se eliminó «{nombre}».")
        return redirect("cinetrack:maratones")
    return redirect("cinetrack:detalle_maraton", pk=pk)


def quitar_de_maraton(request, pk, contenido_id):
    maraton = get_object_or_404(Maraton, pk=pk)
    contenido = get_object_or_404(Contenido, pk=contenido_id)
    if request.method == "POST":
        maraton.contenidos.remove(contenido)
        messages.success(request, f"❌ Quitado «{contenido.titulo}» del maratón.")
    return redirect("cinetrack:detalle_maraton", pk=pk)


class ContenidoViewSet(viewsets.ModelViewSet):
    queryset = Contenido.objects.all()
    serializer_class = ContenidoSerializer
