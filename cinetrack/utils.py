from datetime import datetime
from django.conf import settings
from .models import SagaAlias

import requests
import re, unicodedata


TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/{content_type}"
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

TMDB_CONTENT_TYPES = (
    ("movie", "pelicula"),
    ("tv", "serie"),
)

ARTICULOS = {
    "el", "la", "los", "las",
    "un", "una", "uno", "unos", "unas",
    "the", "a", "an",
    "otro", "otra", "otros", "otras",
}

FRANQUICIAS_1P = {
    "shrek",
}

FRANQUICIAS = {
    "harry potter",
    "star wars",
    "señor anillos",
    "el señor",
    "jurassic park",
    "jurassic world",
    "toy story",
    "rapidos furiosos",
    "rapido furioso",
    "mision imposible",
    "piratas caribe",
    "guardianes galaxia",
    "spider man",
    "spiderman",
}

ROMANOS = {
    "i", "ii", "iii", "iv", "v",
    "vi", "vii", "viii", "ix", "x",
}


def buscar_contenido_tmdb(nombre: str) -> list[dict]:
    """
    Busca películas y series en TMDB y normaliza los resultados
    al formato utilizado internamente por CineTrack.
    """
    resultados = []

    for tipo_api, tipo_valor in TMDB_CONTENT_TYPES:
        resultados.extend(
            _buscar_por_tipo_tmdb(nombre, tipo_api, tipo_valor)
        )

    return resultados


def _buscar_por_tipo_tmdb(
    nombre: str,
    tipo_api: str,
    tipo_valor: str,
) -> list[dict]:
    url = TMDB_SEARCH_URL.format(content_type=tipo_api)
    params = {
        "api_key": settings.TMDB_API_KEY,
        "query": nombre,
        "language": "es-ES",
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException:
        return []

    return [
        normalizado
        for resultado in response.json().get("results", [])
        if (
            normalizado := _normalizar_resultado_tmdb(
                resultado,
                tipo_valor,
            )
        )["titulo"]
    ]


def _normalizar_resultado_tmdb(
    resultado: dict,
    tipo: str,
) -> dict:
    titulo = resultado.get("title") or resultado.get("name")
    resumen = resultado.get("overview") or ""

    fecha_raw = (
        resultado.get("release_date")
        or resultado.get("first_air_date")
    )
    fecha = _parsear_fecha_tmdb(fecha_raw)

    poster_path = resultado.get("poster_path")
    imagen = (
        f"{TMDB_IMAGE_BASE_URL}{poster_path}"
        if poster_path
        else ""
    )

    return {
        "titulo": titulo,
        "resumen": resumen,
        "fecha": fecha,
        "imagen": imagen,
        "tipo": tipo,
    }


def _parsear_fecha_tmdb(fecha_raw: str | None):
    if not fecha_raw:
        return None

    try:
        return datetime.strptime(fecha_raw, "%Y-%m-%d").date()
    except ValueError:
        return None


def quitar_acentos(texto: str) -> str:
    texto_normal = unicodedata.normalize(
        "NFD",
        texto,
    )

    return "".join(
        caracter
        for caracter in texto_normal
        if not unicodedata.combining(caracter)
    )


def clave_saga_desde_titulo(titulo: str) -> str:
    """
    Genera una clave corta de saga a partir del título.
    Ejemplos: "harry potter", "star wars", "jurassic", etc.
    """
    if not titulo:
        return ""

    texto = quitar_acentos(titulo).lower().strip()

    # 2) Cortar subtítulos (antes de :, -, –, —, (, [)
    parte_principal = re.split(r'[:\-\u2013\u2014\(\[]', texto, maxsplit=1)[0].strip()

    # 3) Separar en palabras (solo letras y números)
    palabras = re.findall(r"[a-z0-9]+", parte_principal, flags=re.I)
    if not palabras:
        return ""

    # 4) Quitar artículos iniciales (español/inglés)
    while palabras and palabras[0] in ARTICULOS:
        palabras.pop(0)
    if not palabras:
        return ""

    # Franquicias de 1 palabra (clave directa)
    if palabras and palabras[0] in FRANQUICIAS_1P:
        return palabras[0]

    # 5) Franquicias conocidas (2 palabras)
    if len(palabras) >= 2 and (" ".join(palabras[:2]) in FRANQUICIAS):
        return " ".join(palabras[:2])

    # 6) Limpiar sufijos: parte/temporada/season + número, números, romanos
    base = " ".join(palabras)
    base = re.sub(r"(?:parte|part|temporada|season)\s*\d+$", "", base).strip()
    base = re.sub(r"\d+$", "", base).strip()

    palabras_limpias = base.split()
    if palabras_limpias and palabras_limpias[-1] in ROMANOS:
        palabras_limpias.pop()

    # 7) Regla final
    if len(palabras) >= 2:
        if palabras[1].isdigit() or palabras[1] in ROMANOS:
            return palabras[0]
        return " ".join(palabras[:2])

    return palabras[0]


def nombre_saga_visible(clave: str, fallback: str) -> str:
    alias = SagaAlias.objects.filter(key=clave).first()
    return alias.nombre if alias else fallback


def ordenar_contenidos_saga(contenidos):
    def clave_orden(contenido):
        anio = contenido.fecha.year if contenido.fecha else 9999

        return (
            not bool(contenido.tendra_continuacion),
            anio,
            contenido.titulo.lower(),
        )

    return sorted(contenidos, key=clave_orden)
