from collections import defaultdict
from urllib.parse import unquote

from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Case, Count, IntegerField, Prefetch, Q, When
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.html import escape
from django.views.decorators.http import require_POST

from rest_framework import viewsets

from .content.context import obtener_contexto_grupo_contenido
from .content.views import editar, registrar
from .forms import SagaAliasForm, MaratonForm
from .models import Contenido, SagaAlias, Maraton
from .serializers import ContenidoSerializer
from .utils import buscar_contenido_tmdb, clave_saga_desde_titulo, nombre_saga_visible, ordenar_contenidos_saga


DONUT_CIRCUNFERENCIA = 326
MAXIMO_POR_PLATAFORMA = 5

CALIFICACION_NUMERICA = {
    Contenido.Calificacion.EXCELENTE: 5,
    Contenido.Calificacion.BUENA: 4,
    Contenido.Calificacion.REGULAR: 3,
    Contenido.Calificacion.MALA: 2,
    Contenido.Calificacion.HORRIBLE: 1,
}


def obtener_plataformas(otro_al_final=False):
    plataformas = list(Contenido.Plataforma.choices)

    if not otro_al_final:
        return sorted(
            plataformas,
            key=lambda p: p[1].lower(),
        )

    otras = [
        p
        for p in plataformas
        if p[0] == Contenido.Plataforma.OTRO
    ]

    normales = sorted(
        (
            p
            for p in plataformas
            if p[0] != Contenido.Plataforma.OTRO
        ),
        key=lambda p: p[1].lower(),
    )

    return normales + otras


def con_imagen(queryset):
    return (
        queryset
        .exclude(imagen__isnull=True)
        .exclude(imagen__exact="")
    )


def mensaje_contenido(nombre):
    return f"“{escape(nombre)}”"


# Home
def calcular_promedio_calificacion(qs_contenidos):
    calificaciones = (
        qs_contenidos
        .exclude(calificacion__isnull=True)
        .exclude(calificacion__exact="")
        .values_list("calificacion", flat=True)
    )

    valores = [
        CALIFICACION_NUMERICA[c]
        for c in calificaciones
        if c in CALIFICACION_NUMERICA
    ]

    if not valores:
        return 0.0, 0

    return round(sum(valores) / len(valores), 1), len(valores)


def construir_barras_plataforma(qs_contenidos, total):
    mapa_plataformas = dict(Contenido.Plataforma.choices)

    conteos = (
        qs_contenidos
        .exclude(plataforma__isnull=True)
        .exclude(plataforma__exact="")
        .values("plataforma")
        .annotate(n=Count("id"))
        .order_by("-n")[:5]
    )

    return [
        {
            "nombre": mapa_plataformas.get(fila["plataforma"], fila["plataforma"]),
            "cantidad": fila["n"],
            "porcentaje": int(round((fila["n"] / total) * 100)) if total else 0,
        }
        for fila in conteos
    ]


def obtener_top_calificados():
    return (
        con_imagen(
            Contenido.objects
        )
        .exclude(calificacion__isnull=True)
        .exclude(calificacion__exact="")
        .annotate(
            calificacion_num=Case(
                When(calificacion=Contenido.Calificacion.EXCELENTE, then=5),
                When(calificacion=Contenido.Calificacion.BUENA, then=4),
                When(calificacion=Contenido.Calificacion.REGULAR, then=3),
                When(calificacion=Contenido.Calificacion.MALA, then=2),
                When(calificacion=Contenido.Calificacion.HORRIBLE, then=1),
                default=0,
                output_field=IntegerField(),
            )
        )
        .order_by("-calificacion_num", "-updated_at", "-created_at")[:5]
    )


def obtener_tops_por_plataforma():
    plataformas = sorted(
        Contenido.Plataforma.choices,
        key=lambda p: p[1].lower(),
    )

    tops = []

    for codigo, nombre in plataformas:
        items = (
            con_imagen(
                Contenido.objects.filter(
                    plataforma=codigo,
                    estado=Contenido.Estado.VISTA,
                )
            )
            .order_by("-veces_vista", "-updated_at", "-created_at")[:MAXIMO_POR_PLATAFORMA]
        )

        if items:
            tops.append({
                "codigo": codigo,
                "nombre": nombre,
                "items": items,
            })

    return tops


def home(request):
    qs_contenidos = Contenido.objects.all()

    total = qs_contenidos.count()
    peliculas = qs_contenidos.filter(tipo=Contenido.Tipo.PELICULA).count()
    series = qs_contenidos.filter(tipo=Contenido.Tipo.SERIE).count()
    vistos = qs_contenidos.filter(estado=Contenido.Estado.VISTA).count()
    pendientes = qs_contenidos.filter(estado=Contenido.Estado.PENDIENTE).count()
    favoritas = qs_contenidos.filter(favorita=True).count()

    promedio, calificados = calcular_promedio_calificacion(qs_contenidos)

    porcentaje_promedio = (promedio / 5.0) * 100 if promedio else 0
    desplazamiento_donut = round(
        DONUT_CIRCUNFERENCIA * (1 - porcentaje_promedio / 100),
        2,
    )

    porcentaje_completado = int(round((vistos / total) * 100)) if total else 0

    estadisticas = {
        "total": total,
        "peliculas": peliculas,
        "series": series,
        "vistos": vistos,
        "pendientes": pendientes,
        "promedio": promedio,
        "calificados": calificados,
        "favoritas": favoritas,
    }

    posters_rollo = (
        con_imagen(qs_contenidos)
        .order_by("?")[:64]
    )

    actividad_reciente = (
        con_imagen(qs_contenidos)
        .order_by("-updated_at", "-created_at")[:12]
    )

    return render(request, "cinetrack/home.html", {
        "contenidos": posters_rollo,
        "estadisticas": estadisticas,
        "barras_plataforma": construir_barras_plataforma(qs_contenidos, total),
        "porcentaje_completado": porcentaje_completado,
        "desplazamiento_donut": desplazamiento_donut,
        "actividad_reciente": actividad_reciente,
        "top_calificados": obtener_top_calificados(),
        "tops_plataformas": obtener_tops_por_plataforma(),
    })


# Catálogo
def obtener_filtros_catalogo(request):
    return {
        "tipo": request.GET.get("tipo") or "",
        "plataforma": request.GET.get("plataforma") or "",
        "estado": request.GET.get("estado") or "",
        "favorita": request.GET.get("favorita"),
        "volveria_a_ver": request.GET.get("volveria_a_ver"),
        "buscar": (request.GET.get("buscar") or "").strip(),
    }


def aplicar_filtros_catalogo(queryset, filtros):
    if filtros["volveria_a_ver"] in ("1", "true", "True", "on"):
        queryset = queryset.filter(
            volveria_a_ver=True,
            estado=Contenido.Estado.VISTA,
        )

    if filtros["tipo"]:
        queryset = queryset.filter(tipo=filtros["tipo"])

    if filtros["plataforma"]:
        queryset = queryset.filter(plataforma=filtros["plataforma"])

    if filtros["estado"]:
        queryset = queryset.filter(estado=filtros["estado"])

    if filtros["favorita"] == "1":
        queryset = queryset.filter(favorita=True)

    if filtros["buscar"]:
        queryset = queryset.filter(Q(titulo__icontains=filtros["buscar"]))

    return queryset.order_by("titulo")


def construir_grupos_catalogo(contenidos):
    cubetas = defaultdict(list)

    for item in contenidos:
        cubetas[clave_saga_desde_titulo(item.titulo)].append(item)

    grupos = []

    for clave in sorted(cubetas.keys()):
        items = cubetas[clave]

        if len(items) >= 2:
            items_ordenados = ordenar_contenidos_saga(items)
            representativo = items_ordenados[0]
            base = representativo.titulo.split(":")[0].split("-")[0].strip()
            nombre_visible = nombre_saga_visible(clave, base)

            grupos.append({
                "saga": nombre_visible,
                "items": items_ordenados,
                "count": len(items_ordenados),
                "grouped": True,
                "key": clave,
            })
        else:
            item = items[0]
            grupos.append({
                "saga": item.titulo,
                "items": [item],
                "count": 1,
                "grouped": False,
            })

    return sorted(grupos, key=lambda grupo: grupo["saga"].lower())


def catalogo(request):
    filtros = obtener_filtros_catalogo(request)

    contenidos = aplicar_filtros_catalogo(
        Contenido.objects.all(),
        filtros,
    )

    grupos = construir_grupos_catalogo(contenidos)

    paginador = Paginator(grupos, 24)
    page_obj = paginador.get_page(request.GET.get("page"))

    plataformas_disponibles = obtener_plataformas()
    plataforma_nombre = dict(plataformas_disponibles).get(
        filtros["plataforma"]
    )

    return render(request, "cinetrack/catalogo.html", {
        "buscar": filtros["buscar"],
        "pagina": page_obj.number,
        "page_obj": page_obj,
        "page_groups": page_obj,
        "plataformas": plataformas_disponibles,
        "plataforma_nombre": plataforma_nombre,
        "filtros": filtros,
        "saga_form": SagaAliasForm(),
    })


# CRUD de contenidos
def detalle(request, pk):
    contenido = get_object_or_404(Contenido, pk=pk)
    grupo_ctx = obtener_contexto_grupo_contenido(contenido)

    origen = request.GET.get("origen") or "catalogo"
    pagina = request.GET.get("page")
    maraton_id = request.GET.get("maraton_id")

    return render(request, "cinetrack/detalle.html", {
        "contenido": contenido,
        "origen": origen,
        "page": pagina,
        "maraton_id": maraton_id,
        **grupo_ctx,
    })


@require_POST
def eliminar(request, pk):
    contenido = get_object_or_404(Contenido, pk=pk)
    titulo = contenido.titulo

    contenido.delete()

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse({
            "ok": True,
            "id_eliminado": pk,
            "titulo": titulo,
        })

    messages.success(
        request,
        f"🗑️ {mensaje_contenido(titulo)} fue eliminado correctamente."
    )
    return redirect("cinetrack:catalogo")


# Búsqueda TMDB
def buscar(request):
    resultados = []
    error = None

    if request.method == "POST":
        query = (request.POST.get("query") or "").strip()

        if query:
            resultados = buscar_contenido_tmdb(query)

            if not resultados:
                error = "No se encontraron resultados o TMDB no respondió correctamente."
        else:
            error = "Escribe un título para buscar."

    plataformas_ordenadas = obtener_plataformas(
        otro_al_final=True,
    )

    return render(request, "cinetrack/buscar.html", {
        "resultados": resultados,
        "plataformas": plataformas_ordenadas,
        "error": error,
    })


@require_POST
def guardar_desde_busqueda(request):
    titulo = request.POST.get("titulo")
    plataforma = request.POST.get("plataforma")

    if not titulo or not plataforma:
        messages.error(request, "Faltan datos para guardar el contenido.")
        return redirect("cinetrack:buscar")

    contenido_duplicado = Contenido.objects.filter(
        titulo=titulo,
        plataforma=plataforma,
    ).exists()

    if contenido_duplicado:
        messages.warning(
            request,
            f"⚠️ {mensaje_contenido(titulo)} ya existe en tu lista."
        )
        return redirect("cinetrack:buscar")

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
        estado=request.POST.get("estado") or Contenido.Estado.PENDIENTE,
        tendra_continuacion=request.POST.get("tendra_continuacion") == "on",
        favorita=request.POST.get("favorita") == "on",
    )

    messages.success(
        request,
        f"✅ {mensaje_contenido(titulo)} fue registrada exitosamente."
    )
    return redirect("cinetrack:buscar")


# Kanban / Pendientes
def pendientes(request):
    # Construir columnas Kanban (solo estado=pendiente), usando las fases del modelo
    ICONOS_FASE = {
        "nuevo": "bi-lightning",
        "pronto": "bi-clock",
        "encurso": "bi-play-circle",
        "pausado": "bi-pause-circle",
    }

    fases = []
    for codigo, etiqueta in Contenido.FaseKanban.choices:
        qs = (Contenido.objects
              .filter(estado=Contenido.Estado.PENDIENTE, fase_kanban=codigo)
              .order_by("-updated_at", "titulo"))
        fases.append((codigo, etiqueta, ICONOS_FASE.get(codigo, ""), qs))

    return render(request, "cinetrack/pendientes.html", {"fases": fases})


@require_POST
def mover_fase(request, pk):
    item = get_object_or_404(
        Contenido,
        pk=pk,
        estado=Contenido.Estado.PENDIENTE,
    )
    fase = request.POST.get("fase")

    fases_validas = {c for c, _ in Contenido.FaseKanban.choices}
    if fase not in fases_validas:
        return JsonResponse({"ok": False, "error": "Fase inválida"}, status=400)

    item.fase_kanban = fase
    item.save(update_fields=["fase_kanban", "updated_at"])
    return JsonResponse({"ok": True, "id": item.pk, "fase": item.fase_kanban})


@require_POST
def marcar_vista(request, pk):
    item = get_object_or_404(Contenido, pk=pk)
    item.estado = Contenido.Estado.VISTA
    item.save(update_fields=["estado", "updated_at"])
    return redirect("cinetrack:pendientes")


# Favoritos / Rewatch
def favoritos(request):
    favoritos_qs = Contenido.objects.filter(favorita=True)

    top3 = list(favoritos_qs.order_by("?")[:3])

    peliculas = favoritos_qs.filter(
        tipo=Contenido.Tipo.PELICULA,
    ).order_by("-id")[:20]

    series = favoritos_qs.filter(
        tipo=Contenido.Tipo.SERIE,
    ).order_by("-id")[:20]

    return render(request, "cinetrack/favoritos.html", {
        "top3": top3,
        "peliculas": peliculas,
        "series": series,
    })


@require_POST
def toggle_favorita(request, pk):
    contenido = get_object_or_404(Contenido, pk=pk)
    contenido.favorita = not contenido.favorita
    contenido.save(update_fields=["favorita", "updated_at"])

    return redirect("cinetrack:favoritos")


def volverias(request):
    peliculas = Contenido.objects.filter(
        volveria_a_ver=True,
        tipo=Contenido.Tipo.PELICULA,
    ).order_by("-id")[:14]

    series = Contenido.objects.filter(
        volveria_a_ver=True,
        tipo=Contenido.Tipo.SERIE,
    ).order_by("-id")[:14]

    return render(request, "cinetrack/volveria.html", {
        "peliculas": peliculas,
        "series": series,
    })


# Sagas
def grupo_saga(request, clave: str):
    clave_norm = unquote(unquote(clave))
    page = request.GET.get("page")

    if request.method == "POST":
        nombre = (request.POST.get("nombre") or "").strip()

        if len(nombre) < 3:
            messages.error(
                request,
                "El nombre de la saga es demasiado corto (mínimo 3 caracteres).",
            )
        else:
            SagaAlias.objects.update_or_create(
                key=clave_norm,
                defaults={"nombre": nombre},
            )
            messages.success(
                request,
                f"Nombre de la saga actualizado a “{nombre}”.",
            )

        return redirect(f"{request.path}?page={page}" if page else request.path)

    contenidos = Contenido.objects.all().order_by("titulo")
    items = [
        contenido
        for contenido in contenidos
        if clave_saga_desde_titulo(contenido.titulo) == clave_norm
    ]

    if not items:
        raise Http404("Grupo no encontrado")

    items_ordenados = ordenar_contenidos_saga(items)

    base = items_ordenados[0].titulo.split(":")[0].split("-")[0].strip()
    nombre_visible = nombre_saga_visible(clave_norm, base)

    return render(request, "cinetrack/grupo.html", {
        "saga": nombre_visible,
        "items": items_ordenados,
        "clave": clave_norm,
        "cantidad": len(items_ordenados),
        "page": page,
    })


@require_POST
def renombrar_saga(request):
    form = SagaAliasForm(request.POST)

    if form.is_valid():
        obj, _created = SagaAlias.objects.update_or_create(
            key=form.cleaned_data["key"],
            defaults={
                "nombre": (
                    form.cleaned_data["nombre"].strip()
                    or form.cleaned_data["key"]
                )
            },
        )
        messages.success(request, f"✅ Saga renombrada a “{escape(obj.nombre)}”.")
    else:
        messages.error(request, "No se pudo guardar el nombre de la saga.")

    next_url = (
        request.POST.get("next")
        or request.META.get("HTTP_REFERER")
        or "/cinetrack/catalogo/"
    )
    return redirect(next_url)


# Maratones
def maratones(request):
    lista = (
        Maraton.objects
        .annotate(total_contenidos=Count("contenidos"))
        .prefetch_related(
            Prefetch(
                "contenidos",
                queryset=Contenido.objects.order_by("titulo"),
                to_attr="contenidos_ordenados",
            )
        )
        .order_by("-created_at")
    )

    return render(request, "cinetrack/maratones.html", {
        "maratones": lista,
    })


def detalle_maraton(request, pk):
    maraton = get_object_or_404(Maraton, pk=pk)
    items = maraton.contenidos.order_by("titulo")

    return render(request, "cinetrack/maraton_detalle.html", {
        "maraton": maraton,
        "items": items,
    })


def obtener_contenidos_seleccionados(form, maraton=None):
    if form.is_bound:
        return {
            int(pk)
            for pk in form.data.getlist("contenidos")
            if pk.isdigit()
        }

    if maraton is not None:
        return set(
            maraton.contenidos.values_list("pk", flat=True)
        )

    return set()


def crear_maraton(request):
    if request.method == "POST":
        form = MaratonForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Maratón creado correctamente.")
            return redirect("cinetrack:maratones")
    else:
        form = MaratonForm()

    seleccionados = obtener_contenidos_seleccionados(form)

    return render(request, "cinetrack/maraton_form.html", {
        "form": form,
        "seleccionados": seleccionados,
    })


def editar_maraton(request, pk):
    maraton = get_object_or_404(Maraton, pk=pk)

    if request.method == "POST":
        form = MaratonForm(request.POST, instance=maraton)

        if form.is_valid():
            form.save()
            messages.success(request, "Maratón actualizado.")
            return redirect("cinetrack:maratones")
    else:
        form = MaratonForm(instance=maraton)

    seleccionados = obtener_contenidos_seleccionados(
        form,
        maraton,
    )

    return render(request, "cinetrack/maraton_form.html", {
        "form": form,
        "maraton": maraton,
        "seleccionados": seleccionados,
    })


@require_POST
def eliminar_maraton(request, pk):
    maraton = get_object_or_404(Maraton, pk=pk)
    nombre = maraton.nombre

    maraton.delete()
    messages.success(request, f"🗑️ Se eliminó «{nombre}».")

    return redirect("cinetrack:maratones")


@require_POST
def quitar_de_maraton(request, pk, contenido_id):
    maraton = get_object_or_404(Maraton, pk=pk)
    contenido = get_object_or_404(Contenido, pk=contenido_id)

    maraton.contenidos.remove(contenido)
    messages.success(request, f"❌ Quitado «{contenido.titulo}» del maratón.")

    return redirect("cinetrack:detalle_maraton", pk=pk)


class ContenidoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contenido.objects.all()
    serializer_class = ContenidoSerializer
