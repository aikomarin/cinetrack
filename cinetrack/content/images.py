from urllib.parse import urlsplit


TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"


def resolver_url_portada(valor):
    """Devuelve una URL renderizable para portadas absolutas o paths de TMDB."""
    if not valor:
        return ""

    valor = str(valor).strip()
    if not valor:
        return ""

    partes = urlsplit(valor)
    if partes.scheme in {"http", "https"} and partes.netloc:
        return valor
    if valor.startswith("//"):
        return f"https:{valor}"
    if valor.startswith("/"):
        return f"{TMDB_IMAGE_BASE_URL}{valor}"
    return valor
