# ADR-0002: Separar estado de visualización y fase Kanban

## Estado

Vigente.

## Contexto

El seguimiento general y la organización del tablero responden a preguntas diferentes. `estado` indica si un contenido fue visto o continúa pendiente, mientras que `fase_kanban` indica la etapa de intención de visualización de un contenido pendiente.

La interfaz Kanban muestra contenidos pendientes. Una solicitud construida fuera de la interfaz podría intentar mover de fase un contenido ya visto.

## Decisión

Mantener `estado` y `fase_kanban` como campos independientes de `Contenido`.

Los puntos de escritura del flujo Kanban deben validar en backend que el contenido sea pendiente antes de modificar su fase. La vista `mover_fase` aplica actualmente esta validación.

## Consecuencias

- El historial general de visualización no queda acoplado a las etapas del tablero.
- El tablero puede organizar exclusivamente los contenidos pendientes.
- El esquema no contiene una constraint cruzada entre ambos campos, por lo que los puntos de escritura deben conservar la regla de coherencia.
- Otras operaciones sobre `Contenido` podrían producir combinaciones incoherentes si omiten esa validación.

## Alternativas consideradas

Representar el estado general y la etapa Kanban mediante un único campo. Esta alternativa mezclaría dos dimensiones diferentes del seguimiento.

