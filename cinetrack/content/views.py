from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from ..models import Contenido
from .context import obtener_contexto_grupo_contenido
from .forms import ContenidoForm
from .navigation import (
    obtener_retorno_catalogo,
    obtener_retorno_favoritos,
    url_con_pagina,
)


ORIGEN_CATALOGO = "catalogo"
ORIGEN_GRUPO = "grupo"
ORIGEN_FAVORITOS = "favoritos"


def _obtener_url_retorno_editar(
    contenido,
    origen,
    pagina,
    retorno_catalogo,
    retorno_favoritos,
    grupo_ctx,
):
    if origen == ORIGEN_CATALOGO:
        return (
            retorno_catalogo
            or url_con_pagina("cinetrack:catalogo", pagina)
        )
    if origen == ORIGEN_GRUPO and grupo_ctx["en_grupo"]:
        return url_con_pagina(
            "cinetrack:grupo_saga",
            pagina,
            args=[grupo_ctx["clave_saga"]],
        )
    if origen == ORIGEN_FAVORITOS:
        return (
            retorno_favoritos
            or reverse("cinetrack:favoritos")
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
    retorno_catalogo = obtener_retorno_catalogo(request)
    retorno_favoritos = obtener_retorno_favoritos(request)
    url_retorno = _obtener_url_retorno_editar(
        contenido,
        origen,
        pagina,
        retorno_catalogo,
        retorno_favoritos,
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
        "retorno_favoritos": retorno_favoritos,
        "url_retorno": url_retorno,
        **grupo_ctx,
    })
