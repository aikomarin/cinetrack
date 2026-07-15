# Changelog de CineTrack

Este documento registra cambios verificables con impacto en el producto o en la operación del proyecto. La planificación futura se mantiene en el roadmap.

## Unreleased

No hay cambios registrados.

## 2026-07-15

### Documentation

- Se reorganizó y consolidó la documentación técnica y de producto de CineTrack.

## 2026-07-13

### Changed

- Se incorporaron ordenamientos predeterminados para `Contenido`, `SagaAlias` y `Maraton`.
- La etiqueta `HBO Max` fue actualizada a `HBO`.
- Star+ fue eliminado de las plataformas disponibles después de migrar sus registros a Disney+.

### Infrastructure

- Se preparó la configuración de producción para PostgreSQL y el servicio de archivos estáticos con WhiteNoise.

## 2026-07-08

### Changed

- Se reemplazaron las listas de choices de `Contenido` por `models.TextChoices`.
- `veces_vista` fue modificado de `IntegerField` a `PositiveIntegerField`.
- Se incorporó una migración de datos para transformar los registros con `plataforma="star"` a `plataforma="disney"`.
