from django import template

from ..content.images import resolver_url_portada


register = template.Library()


@register.filter
def portada_url(valor):
    return resolver_url_portada(valor)
