# Changelog de CineTrack

## 2026-07-08

### Changed

- Se reemplazaron las listas de choices de `Contenido` por `models.TextChoices`.
- `veces_vista` fue modificado de `IntegerField` a `PositiveIntegerField`.
- La etiqueta `HBO Max` fue actualizada a `HBO`.
- Los registros asociados a Star+ fueron migrados a Disney+.
- Star+ fue eliminado de las plataformas disponibles.

### Technical

- Se creó una migración de datos para transformar `plataforma="star"` en `plataforma="disney"`.
- Se actualizaron las referencias a choices del modelo para utilizar las nuevas clases `TextChoices`.