# ADR-0003: Definir explícitamente el contrato serializado de `Contenido`

## Estado

Vigente.

## Contexto

La implementación inicial de `ContenidoSerializer` utilizaba `fields = "__all__"`. Con esa configuración, cualquier campo incorporado al modelo podía aparecer automáticamente en la representación REST.

El serializer forma parte del contrato público de la API y sus cambios deben ser intencionales.

## Decisión

Enumerar explícitamente en `ContenidoSerializer` los campos expuestos por la API.

Declarar `id`, `created_at` y `updated_at` como campos de solo lectura del serializer.

## Consecuencias

- Añadir un campo al modelo no lo expone automáticamente mediante REST.
- Los cambios del contrato requieren actualizar de forma deliberada el serializer y su documentación.
- Los campos administrados por el sistema quedan identificados como no editables por el serializer.
- El comportamiento de solo lectura de toda la API depende además del ViewSet utilizado.

## Alternativas consideradas

Utilizar `fields = "__all__"`. Esta alternativa reduce mantenimiento manual, pero permite modificar el contrato como efecto secundario de un cambio en el modelo.

