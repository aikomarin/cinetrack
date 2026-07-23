from collections import defaultdict

from django.db.models import Q

from ..models import Contenido
from ..utils import (
    clave_saga_desde_titulo,
    nombre_saga_visible,
    ordenar_contenidos_saga,
)


def aplicar_filtros_catalogo(queryset, filtros):
    if filtros["volveria_a_ver"] == "1":
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
        queryset = queryset.filter(
            Q(titulo__icontains=filtros["buscar"])
        )

    return queryset.order_by("titulo")


def construir_grupos_catalogo(contenidos):
    cubetas = defaultdict(list)
    for item in contenidos:
        cubetas[clave_saga_desde_titulo(item.titulo)].append(item)

    grupos = []
    for clave, items in cubetas.items():
        if len(items) >= 2:
            items_ordenados = ordenar_contenidos_saga(items)
            representativo = items_ordenados[0]
            base = representativo.titulo.split(":")[0].split("-")[0].strip()
            grupos.append({
                "saga": nombre_saga_visible(clave, base),
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
