VENTANA_PAGINAS = 5


def obtener_rango_paginas(pagina_actual, total_paginas):
    cantidad = min(VENTANA_PAGINAS, total_paginas)
    inicio = max(1, pagina_actual - 2)
    fin = min(total_paginas, inicio + cantidad - 1)
    inicio = max(1, fin - cantidad + 1)
    return range(inicio, fin + 1)


def url_con_pagina(parametros, numero_pagina):
    query = parametros.copy()
    query["page"] = numero_pagina
    return f"?{query.urlencode()}"


def construir_paginacion(parametros, page_obj):
    paginas = [
        {
            "numero": numero,
            "actual": numero == page_obj.number,
            "url": url_con_pagina(parametros, numero),
        }
        for numero in obtener_rango_paginas(
            page_obj.number,
            page_obj.paginator.num_pages,
        )
    ]

    return {
        "paginas": paginas,
        "primera": (
            url_con_pagina(parametros, 1)
            if page_obj.has_previous()
            else None
        ),
        "anterior": (
            url_con_pagina(
                parametros,
                page_obj.previous_page_number(),
            )
            if page_obj.has_previous()
            else None
        ),
        "siguiente": (
            url_con_pagina(
                parametros,
                page_obj.next_page_number(),
            )
            if page_obj.has_next()
            else None
        ),
        "ultima": (
            url_con_pagina(
                parametros,
                page_obj.paginator.num_pages,
            )
            if page_obj.has_next()
            else None
        ),
    }
