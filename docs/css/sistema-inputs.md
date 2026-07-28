# Sistema de Inputs y Selects de CineTrack

## Objetivo

Los inputs y selects constituyen el sistema base de captura de información en CineTrack.

Todos los campos de formulario deberán compartir una identidad visual única y consistente en todo el proyecto.

---

## Alcance

Este sistema aplica a:

- Inputs de texto.
- Inputs numéricos.
- Inputs de búsqueda.
- Selects nativos.
- Selectores personalizados.
- Textareas.
- Campos readonly.
- Campos disabled.

Los campos de fecha gestionados mediante Flatpickr se documentan de forma independiente en:

- `docs/css/sistema-flatpickr.md`

Los placeholders se documentan en:

- `docs/css/sistema-placeholders.md`

---

## Tipografía

La tipografía deberá respetar lo definido en:

- `docs/css/sistema-tipografico-global.md`

Los placeholders deberán respetar lo definido en:

- `docs/css/sistema-placeholders.md`

---

# Especificación visual

Todos los campos deberán compartir los mismos valores para:

- Altura.
- Padding interno.
- Familia tipográfica.
- Tamaño del texto.
- Peso tipográfico.
- Color del texto.
- Fondo.
- Borde.
- Radio.
- Transiciones.

No deberán existir variantes visuales entre formularios.

---

## Estados

Todos los campos deberán utilizar el mismo sistema de estados.

### Normal

Estado base oficial del sistema.

### Hover

El borde podrá reforzarse visualmente de forma consistente con el resto de los campos.

### Focus

El foco deberá utilizar el estilo oficial del sistema.

No deberá:

- Modificar la altura.
- Alterar el layout.
- Cambiar el tamaño del borde.

### Disabled

Los campos deshabilitados deberán mantener coherencia con el resto del sistema.

### Readonly

Los campos readonly deberán diferenciarse visualmente sin confundirse con un campo deshabilitado.

### Error

Todos los errores deberán utilizar el sistema oficial de validaciones del proyecto.

No deberán existir variantes específicas por formulario.

---

## Selects

Los selects deberán compartir el mismo sistema visual que los inputs.

Esto incluye:

- Altura.
- Padding.
- Tipografía.
- Color.
- Fondo.
- Borde.
- Radio.
- Estados.
- Focus.

Las diferencias propias del navegador deberán minimizarse únicamente cuando sea necesario para mantener la coherencia visual.

---

## Selectores personalizados

Los selectores personalizados deberán integrarse visualmente con este sistema.

Podrán conservar únicamente las reglas necesarias para su funcionamiento.

No deberán redefinir:

- Tipografía.
- Tamaño.
- Colores.
- Bordes.
- Estados.
- Radio.

---

## Implementación

Los estilos deberán centralizarse utilizando las reglas globales del sistema de formularios.

Las páginas únicamente podrán modificar aspectos de composición, por ejemplo:

- Márgenes.
- Distribución.
- Ancho de columnas.
- Posición dentro del layout.

No deberán modificar:

- Altura.
- Padding.
- Tipografía.
- Tamaño.
- Peso.
- Fondo.
- Borde.
- Radio.
- Focus.
- Glow.
- Estados visuales.

Se deberán eliminar reglas duplicadas siempre que sea posible.

---

## Fuera de alcance

Esta implementación no deberá modificar:

- Labels.
- Botones.
- Placeholders.
- Flatpickr.
- Modelos.
- Forms.
- Views.
- Validaciones.
- JavaScript.
- Estructura HTML de los formularios, salvo que sea estrictamente necesario.