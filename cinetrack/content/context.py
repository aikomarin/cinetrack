from ..models import Contenido
from ..utils import clave_saga_desde_titulo


def obtener_contexto_grupo_contenido(contenido):
    clave_saga = clave_saga_desde_titulo(contenido.titulo)
    titulos = (
        Contenido.objects
        .exclude(titulo__isnull=True)
        .values_list("titulo", flat=True)
    )
    en_grupo = sum(
        1
        for titulo in titulos
        if clave_saga_desde_titulo(titulo) == clave_saga
    ) > 1

    return {
        "en_grupo": en_grupo,
        "clave_saga": clave_saga if en_grupo else None,
    }
