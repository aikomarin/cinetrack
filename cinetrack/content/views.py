from urllib.parse import urlencode

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import Resolver404, resolve, reverse
from django.utils.http import url_has_allowed_host_and_scheme

from ..models import Contenido
from .context import obtener_contexto_grupo_contenido
from .forms import ContenidoForm


ORIGEN_CATALOGO = "catalogo"
ORIGEN_GRUPO = "grupo"


def _url_con_pagina(nombre_url, pagina, *, args=None):
    url = reverse(nombre_url, args=args)
    if pagina:
        return f"{url}?{urlencode({'page': pagina})}"
    return url


def _obtener_retorno_catalogo(request):
    retorno = request.GET.get("return_to")
    if not retorno or not url_has_allowed_host_and_scheme(
        retorno,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return None

    try:
        coincidencia = resolve(retorno.split("?", 1)[0])
    except Resolver404:
        return None

    if coincidencia.view_name != "cinetrack:catalogo":
        return None
    return retorno


def _obtener_url_retorno_editar(
    contenido,
    origen,
    pagina,
    retorno_catalogo,
    grupo_ctx,
):
    if origen == ORIGEN_CATALOGO:
        return (
            retorno_catalogo
            or _url_con_pagina("cinetrack:catalogo", pagina)
        )
    if origen == ORIGEN_GRUPO and grupo_ctx["en_grupo"]:
        return _url_con_pagina(
            "cinetrack:grupo_saga",
            pagina,
            args=[grupo_ctx["clave_saga"]],
        )
    return reverse("cinetrack:detalle", args=[contenido.pk])


def registrar(request):
    if request.method == "POST":
        formulario = ContenidoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("cinetrack:catalogo")
    else:
        formulario = ContenidoForm()

    return render(request, "cinetrack/registrar.html", {
        "formulario": formulario,
    })


def editar(request, pk):
    contenido = get_object_or_404(Contenido, pk=pk)
    grupo_ctx = obtener_contexto_grupo_contenido(contenido)
    origen = request.GET.get("origen")
    pagina = request.GET.get("page")
    retorno_catalogo = _obtener_retorno_catalogo(request)
    url_retorno = _obtener_url_retorno_editar(
        contenido,
        origen,
        pagina,
        retorno_catalogo,
        grupo_ctx,
    )

    if request.method == "POST":
        formulario = ContenidoForm(request.POST, instance=contenido)
        if formulario.is_valid():
            formulario.save()
            return redirect(url_retorno)
    else:
        formulario = ContenidoForm(instance=contenido)

    return render(request, "cinetrack/editar.html", {
        "contenido": contenido,
        "formulario": formulario,
        "origen": origen,
        "page": pagina,
        "retorno_catalogo": retorno_catalogo,
        "url_retorno": url_retorno,
        **grupo_ctx,
    })
