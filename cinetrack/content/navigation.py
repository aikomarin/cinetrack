from urllib.parse import urlencode

from django.urls import Resolver404, resolve, reverse
from django.utils.http import url_has_allowed_host_and_scheme


def url_con_pagina(nombre_url, pagina, *, args=None):
    url = reverse(nombre_url, args=args)
    if pagina:
        return f"{url}?{urlencode({'page': pagina})}"
    return url


def obtener_retorno_catalogo(request):
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
