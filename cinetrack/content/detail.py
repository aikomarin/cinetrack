from urllib.parse import urlencode

from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from ..models import Contenido
from .context import obtener_contexto_grupo_contenido
from .navigation import (
    obtener_retorno_catalogo,
    obtener_retorno_favoritos,
    url_con_pagina,
)


def _obtener_navegacion_detalle(
    origen,
    pagina,
    maraton_id,
    retorno_catalogo,
    retorno_favoritos,
    grupo_ctx,
):
    if origen == "maraton" and maraton_id:
        return reverse("cinetrack:detalle_maraton", args=[maraton_id]), "Volver al maratón"
    if origen == "grupo" and grupo_ctx["clave_saga"]:
        return (
            url_con_pagina(
                "cinetrack:grupo_saga",
                pagina,
                args=[grupo_ctx["clave_saga"]],
            ),
            "Volver al grupo",
        )
    if origen == "favoritos":
        return (
            retorno_favoritos
            or reverse("cinetrack:favoritos"),
            "Volver a favoritos",
        )
    if origen == "pendientes":
        return reverse("cinetrack:pendientes"), "Volver a pendientes"
    if origen == "volveria_a_ver":
        return reverse("cinetrack:volverias"), "Regresar a Volverías a Ver"
    if grupo_ctx["en_grupo"] and grupo_ctx["clave_saga"]:
        return (
            url_con_pagina(
                "cinetrack:grupo_saga",
                pagina,
                args=[grupo_ctx["clave_saga"]],
            ),
            "Volver al grupo",
        )
    return (
        retorno_catalogo
        or url_con_pagina("cinetrack:catalogo", pagina),
        "Volver al catálogo",
    )


def detalle(request, pk):
    contenido = get_object_or_404(Contenido, pk=pk)
    grupo_ctx = obtener_contexto_grupo_contenido(contenido)
    origen = request.GET.get("origen") or "catalogo"
    pagina = request.GET.get("page")
    maraton_id = request.GET.get("maraton_id")
    retorno_catalogo = obtener_retorno_catalogo(request)
    retorno_favoritos = obtener_retorno_favoritos(request)
    url_retorno, texto_retorno = _obtener_navegacion_detalle(
        origen,
        pagina,
        maraton_id,
        retorno_catalogo,
        retorno_favoritos,
        grupo_ctx,
    )

    if origen == "favoritos":
        parametros_editar = {
            "origen": "favoritos",
            "return_to": retorno_favoritos or url_retorno,
        }
        url_editar = (
            reverse("cinetrack:editar", args=[contenido.pk])
            + f"?{urlencode(parametros_editar)}"
        )
    else:
        url_editar = (
            reverse("cinetrack:editar", args=[contenido.pk])
            + "?origen=detalle"
        )

    return render(request, "cinetrack/detalle.html", {
        "contenido": contenido,
        "url_retorno": url_retorno,
        "texto_retorno": texto_retorno,
        "url_editar": url_editar,
        **grupo_ctx,
    })
