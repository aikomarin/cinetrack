# ADR-0007: Exponer la API REST de `Contenido` como solo lectura

## Estado

Vigente.

## Contexto

La implementación inicial utilizaba `ModelViewSet`, que habilitaba operaciones de lectura y escritura sobre `Contenido`. La API actual no cuenta con un mecanismo específico de autenticación y permisos para proteger mutaciones REST.

## Decisión

Exponer `Contenido` mediante `ReadOnlyModelViewSet`.

La API permite listar y consultar contenidos, pero no crear, actualizar o eliminar registros mediante REST.

## Consecuencias

- Los clientes pueden consultar la colección y sus elementos individuales.
- Las mutaciones continúan realizándose mediante los flujos internos de la interfaz web.
- El permiso efectivo actual es `AllowAny`, por lo que las consultas no requieren autenticación.
- Habilitar escritura REST o exigir autenticación requeriría revisar esta decisión y el contrato de la API.

## Alternativas consideradas

Mantener `ModelViewSet` con las operaciones de escritura habilitadas. Sin permisos específicos, esa alternativa exponía modificaciones de datos a través de la API.

