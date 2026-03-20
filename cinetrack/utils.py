import requests
from django.conf import settings
from datetime import datetime


def buscar_contenido_tmdb(nombre: str):
    """
    Busca películas o series en TMDb según el nombre dado.
    Retorna una lista de dicts con: titulo, resumen, fecha, imagen y tipo.
    """
    tipos = [("movie", "pelicula"), ("tv", "serie")]
    resultados = []

    for tipo_api, tipo_valor in tipos:
        url = f"https://api.themoviedb.org/3/search/{tipo_api}"
        params = {
            "api_key": settings.TMDB_API_KEY,
            "query": nombre,
            "language": "es-ES",
        }

        resp = requests.get(url, params=params)
        if resp.status_code != 200:
            continue

        for r in resp.json().get("results", []):
            titulo = r.get("title") or r.get("name")
            resumen = r.get("overview")

            # Fecha (puede venir como release_date o first_air_date)
            fecha_raw = r.get("release_date") or r.get("first_air_date")
            try:
                fecha = datetime.strptime(fecha_raw, "%Y-%m-%d").date() if fecha_raw else None
            except ValueError:
                fecha = None

            imagen = r.get("poster_path")
            imagen_url = f"https://image.tmdb.org/t/p/w500{imagen}" if imagen else ""

            resultados.append({
                "titulo": titulo,
                "resumen": resumen,
                "fecha": fecha,
                "imagen": imagen_url,
                "tipo": tipo_valor,
            })

    return resultados
