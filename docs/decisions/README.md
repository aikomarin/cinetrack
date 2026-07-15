# Decisiones técnicas de CineTrack

## Propósito

Este directorio registra decisiones técnicas duraderas de CineTrack. Cada ADR conserva el contexto conocido, la decisión adoptada, sus consecuencias y, cuando existe evidencia suficiente, las alternativas consideradas.

Los ADRs explican por qué se eligió una solución. La descripción detallada del sistema vigente permanece en la documentación especializada.

## Estados

- **Vigente:** la decisión continúa aplicándose.
- **Sustituida:** otra decisión posterior reemplazó su aplicación.
- **Obsoleta:** la decisión dejó de ser aplicable sin ser sustituida por otra.
- **Pendiente de aclaración:** la intención o el alcance necesitan confirmación.

## Índice de decisiones

| ADR | Decisión | Estado |
| --- | --- | --- |
| [0001](0001-use-textchoices-for-controlled-values.md) | Usar `TextChoices` para valores controlados | Vigente |
| [0002](0002-separate-viewing-status-and-kanban-phase.md) | Separar estado de visualización y fase Kanban | Vigente |
| [0003](0003-define-explicit-content-api-schema.md) | Definir explícitamente el contrato serializado de `Contenido` | Vigente |
| [0004](0004-normalize-tmdb-responses-at-integration-boundary.md) | Normalizar respuestas de TMDB en el límite de integración | Vigente |
| [0005](0005-infer-sagas-from-content-titles.md) | Inferir sagas desde títulos y permitir alias | Vigente |
| [0006](0006-protect-web-writes-with-post-and-csrf.md) | Proteger escrituras web mediante POST y CSRF | Vigente |
| [0007](0007-expose-content-rest-api-as-read-only.md) | Exponer la API REST de `Contenido` como solo lectura | Vigente |

