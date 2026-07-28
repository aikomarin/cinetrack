from urllib.parse import urlencode, urlsplit, urlunsplit

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import QueryDict
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.html import escape
from django.views.decorators.http import require_POST

from ..forms import BuscarContenidoForm
from ..models import Contenido
from ..utils import buscar_contenido_tmdb
from .filters import aplicar_filtros_catalogo, construir_grupos_catalogo
from .forms import CatalogoFiltrosForm, ContenidoDesdeBusquedaForm
from .pagination import construir_paginacion_catalogo


CATALOGO_POR_PAGINA = 24


def obtener_plataformas(*, otro_al_final=False):
    plataformas = list(Contenido.Plataforma.choices)
    if not otro_al_final:
        return sorted(plataformas, key=lambda opcion: opcion[1].lower())

    normales = sorted(
        (
            opcion
            for opcion in plataformas
            if opcion[0] != Contenido.Plataforma.OTRO
        ),
        key=lambda opcion: opcion[1].lower(),
    )
    otras = [
        opcion
        for opcion in plataformas
        if opcion[0] == Contenido.Plataforma.OTRO
    ]
    return normales + otras


def normalizar_pagina_retorno_catalogo(retorno):
    partes = urlsplit(retorno)
    parametros = QueryDict(partes.query, mutable=True)
    pagina_solicitada = parametros.get("page")

    try:
        numero_pagina = int(pagina_solicitada)
    except (TypeError, ValueError):
        return retorno

    filtros = CatalogoFiltrosForm(parametros).filtros_validos()
    contenidos = aplicar_filtros_catalogo(Contenido.objects.all(), filtros)
    grupos = construir_grupos_catalogo(contenidos)
    ultima_pagina = Paginator(grupos, CATALOGO_POR_PAGINA).num_pages

    if numero_pagina <= ultima_pagina:
        return retorno

    parametros["page"] = ultima_pagina
    return urlunsplit((
        partes.scheme,
        partes.netloc,
        partes.path,
        parametros.urlencode(),
        partes.fragment,
    ))


def catalogo(request):
    formulario_filtros = CatalogoFiltrosForm(request.GET or None)
    filtros = formulario_filtros.filtros_validos()
    contenidos = list(
        aplicar_filtros_catalogo(Contenido.objects.all(), filtros)
    )
    grupos = construir_grupos_catalogo(contenidos)
    page_obj = Paginator(grupos, CATALOGO_POR_PAGINA).get_page(
        request.GET.get("page")
    )

    plataformas = obtener_plataformas()
    return render(request, "cinetrack/catalogo.html", {
        "buscar": filtros["buscar"],
        "page_obj": page_obj,
        "page_groups": page_obj,
        "plataformas": plataformas,
        "plataforma_nombre": dict(plataformas).get(filtros["plataforma"]),
        "filtros": filtros,
        "paginacion": construir_paginacion_catalogo(
            request.GET,
            page_obj,
        ),
        "total_contenidos": len(contenidos),
    })


def buscar(request):
    datos = request.POST if request.method == "POST" else request.GET
    busqueda_realizada = bool(datos)
    formulario = BuscarContenidoForm(datos or None)
    resultados = []

    if busqueda_realizada and formulario.is_valid():
        resultados = buscar_contenido_tmdb(
            formulario.cleaned_data["query"]
        )

    return render(request, "cinetrack/buscar.html", {
        "resultados": resultados,
        "plataformas": obtener_plataformas(otro_al_final=True),
        "formulario_busqueda": formulario,
        "busqueda_realizada": busqueda_realizada,
        "query": datos.get("query", "").strip(),
    })


def _url_busqueda(query):
    url = reverse("cinetrack:buscar")
    if query:
        return f"{url}?{urlencode({'query': query})}"
    return url


@require_POST
def guardar_desde_busqueda(request):
    query = (request.POST.get("query") or "").strip()
    formulario = ContenidoDesdeBusquedaForm(request.POST)

    if not formulario.is_valid():
        if formulario.non_field_errors():
            titulo = escape(request.POST.get("titulo") or "")
            messages.warning(
                request,
                f"“{titulo}” ya existe en tu lista.",
            )
            return redirect(_url_busqueda(query))

        mensaje = next(iter(formulario.errors.values()))[0]
        messages.error(request, f"No se pudo guardar: {mensaje}")
        return redirect(_url_busqueda(query))

    contenido = formulario.save()
    messages.success(
        request,
        f"“{escape(contenido.titulo)}” fue registrada exitosamente.",
    )
    return redirect(_url_busqueda(query))
