# Sistema de Switches de CineTrack

## Objetivo

Los switches representan opciones booleanas dentro de los formularios de CineTrack.

Todos los switches deberán compartir una única identidad visual y un comportamiento consistente en todo el proyecto.

---

## Alcance

Este sistema aplica a:

- Switches de formularios.
- Switches de búsqueda y filtros.
- Switches dentro de componentes reutilizables.
- Cualquier interruptor de tipo on/off implementado en la interfaz.

No aplica a:

- Checkboxes.
- Radio buttons.
- Controles de selección múltiple.

---

## Tipografía

La etiqueta asociada al switch deberá respetar lo definido en:

- `docs/css/sistema-labels.md`

---

# Especificación visual

Todos los switches deberán compartir los mismos valores para:

- Ancho.
- Alto.
- Radio.
- Tamaño de la perilla.
- Colores.
- Bordes.
- Sombras.
- Transiciones.
- Separación entre el switch y su label.

No deberán existir variantes visuales entre formularios.

---

## Estados

Todos los switches deberán utilizar el mismo sistema de estados.

### Inactivo

Estado base del sistema.

### Hover

Deberá mantener el mismo comportamiento visual en todo el proyecto.

### Focus

El foco deberá ser consistente con el resto de los controles del sistema.

No deberá modificar:

- Tamaño.
- Layout.
- Posición del switch.

### Activo

Todos los switches deberán utilizar el mismo color y la misma posición de la perilla.

### Disabled

Los switches deshabilitados deberán mantener coherencia con el resto del sistema.

---

## Label asociada

La separación entre el switch y su label deberá ser consistente.

La label deberá mantener:

- Tipografía.
- Tamaño.
- Peso.
- Color.

No deberán existir variantes específicas para cada formulario.

---

## Composición

El sistema de switches define únicamente el componente.

Cada página podrá modificar únicamente aspectos de composición, por ejemplo:

- Márgenes.
- Distribución dentro del layout.
- Número de columnas.
- Centrado del grupo de switches cuando el diseño lo requiera.

No deberá modificar:

- Tamaño del switch.
- Colores.
- Bordes.
- Estados.
- Tipografía de la label.
- Separación entre switch y label.

---

## Implementación

El sistema deberá centralizarse utilizando un único componente reutilizable.

Las páginas no deberán redefinir la apariencia visual de los switches.

Se deberán eliminar reglas duplicadas siempre que sea posible.

---

## Fuera de alcance

Esta implementación no deberá modificar:

- Inputs.
- Selects.
- Placeholders.
- Flatpickr.
- Botones.
- Labels.
- Modelos.
- Forms.
- Views.
- Validaciones.
- JavaScript.
- Estructura HTML de los formularios, salvo que sea estrictamente necesario.