# ADR-0005: Inferir sagas desde títulos y permitir alias

## Estado

Vigente.

## Contexto

CineTrack necesita agrupar contenidos relacionados para presentarlos como sagas. El modelo actual no contiene una entidad `Saga` ni una relación persistida entre una saga y `Contenido`.

Los títulos contienen información que permite inferir muchas de esas agrupaciones, aunque el nombre calculado no siempre es el más claro para su presentación.

## Decisión

Calcular dinámicamente una clave de saga a partir del título del contenido.

Utilizar `SagaAlias` para asociar una clave calculada con un nombre visible personalizado sin convertir la agrupación en una relación persistida con `Contenido`.

## Consecuencias

- No es necesario administrar manualmente la pertenencia de cada contenido a una saga.
- La pertenencia depende de heurísticas aplicadas a los títulos.
- Algunos contenidos pueden agruparse incorrectamente o no ser reconocidos como parte de una saga.
- Un alias modifica el nombre visible, pero no cambia la clave ni la pertenencia calculada.

## Alternativas consideradas

Crear una entidad `Saga` y relacionarla explícitamente con `Contenido`. Esa alternativa ofrecería pertenencia persistida, pero requeriría administrarla directamente en el modelo de datos.

