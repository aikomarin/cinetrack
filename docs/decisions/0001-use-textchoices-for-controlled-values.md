# ADR-0001: Usar `TextChoices` para valores controlados

## Estado

Vigente.

## Contexto

La implementación inicial definía los choices de Django mediante listas de tuplas. Diferentes partes de la aplicación necesitaban reutilizar valores internos como `pendiente`, `vista`, `nuevo` o `encurso`.

Mantener esos valores como strings literales dispersos dificulta identificar el conjunto válido y aumenta el riesgo de inconsistencias.

## Decisión

Definir los valores controlados de tipo, estado, plataforma, calificación y fase Kanban mediante clases `models.TextChoices` dentro de `Contenido`.

El resto del código debe utilizar las constantes proporcionadas por esas clases cuando necesite referirse a un valor controlado.

## Consecuencias

- Los valores internos y sus etiquetas visibles permanecen centralizados.
- El código puede reutilizar constantes con nombres explícitos en lugar de repetir strings.
- La lista de valores vigente se mantiene junto al modelo que la utiliza.
- Cambiar un valor almacenado puede requerir una migración de datos, además de actualizar el choice.

## Alternativas consideradas

Mantener listas de tuplas y utilizar directamente los valores literales. Esta era la implementación anterior y no ofrecía constantes reutilizables asociadas al modelo.

