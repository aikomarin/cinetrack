# ADR-0004: Normalizar respuestas de TMDB en el límite de integración

## Estado

Vigente.

## Contexto

TMDB representa películas y series mediante estructuras parcialmente diferentes. El título y la fecha, por ejemplo, se obtienen de campos distintos según el tipo de recurso consultado.

Permitir que las vistas interpreten directamente esas variantes propagaría detalles del proveedor por la aplicación.

## Decisión

Transformar las respuestas de TMDB a una representación interna común antes de entregarlas a las vistas de CineTrack.

La comunicación HTTP y la adaptación de la respuesta permanecen en el límite de integración. Actualmente este comportamiento está implementado mediante funciones auxiliares en `cinetrack/utils.py`.

## Consecuencias

- Las vistas trabajan con la misma estructura para películas y series.
- Los detalles propios de TMDB se concentran en el código de integración.
- Los cambios del proveedor requieren mantener el mapeo hacia la representación interna.
- La ubicación física actual en `utils.py` puede cambiar sin alterar la decisión de normalizar en el límite.

## Alternativas consideradas

Interpretar las estructuras de TMDB directamente en cada vista o consumidor. Esta alternativa acoplaría esos componentes a las diferencias del proveedor.

