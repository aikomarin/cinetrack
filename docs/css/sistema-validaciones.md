# Sistema de Validaciones de CineTrack

## Objetivo

Las validaciones comunican al usuario que un formulario no puede completarse debido a uno o varios errores.

Todos los errores de validación deberán compartir una única identidad visual y un comportamiento consistente en todo el proyecto.

---

## Alcance

Este sistema aplica a:

- Errores inline asociados a un campo.
- Errores generales de un formulario.
- Listas de errores generadas por Django (`errorlist`).

No aplica a:

- Mensajes globales.
- Modales de confirmación.
- Estados vacíos.
- Indicadores de carga.

---

## Tipografía

La tipografía deberá respetar lo definido en:

- `docs/css/sistema-tipografico-global.md`

---

# Especificación visual

Todos los errores deberán compartir:

- Color.
- Tipografía.
- Tamaño del texto.
- Peso tipográfico.
- Iconografía.
- Separación respecto al campo.
- Espaciado interno cuando exista un contenedor.
- Jerarquía visual.

No deberán existir variantes específicas por formulario.

---

## Error de campo

Los errores asociados directamente a un campo deberán:

- Mantener proximidad con el control correspondiente.
- Utilizar el icono oficial del sistema.
- Compartir el mismo color y tipografía.
- Presentarse siempre con la misma separación respecto al campo.

---

## Error general del formulario

Cuando un formulario tenga errores generales, deberá utilizar un único componente reutilizable.

Este componente deberá compartir:

- Geometría.
- Color.
- Tipografía.
- Iconografía.
- Espaciado.

No deberán existir variantes distintas según la funcionalidad.

---

## Listas de errores

Las listas generadas por Django deberán presentar un estilo uniforme.

No deberán depender del estilo predeterminado del navegador.

---

## Implementación

El sistema deberá centralizarse utilizando componentes reutilizables.

Las páginas únicamente podrán modificar aspectos de composición cuando sean necesarios para el layout.

No deberán redefinir:

- Colores.
- Tipografía.
- Iconografía.
- Tamaños.
- Espaciados.
- Estilo visual.

Se deberán eliminar reglas duplicadas siempre que sea posible.

---

## Fuera de alcance

Esta implementación no deberá modificar:

- Mensajes globales.
- Botones.
- Inputs.
- Labels.
- Placeholders.
- Flatpickr.
- Modelos.
- Forms.
- Views.
- Validaciones de negocio.
- JavaScript.