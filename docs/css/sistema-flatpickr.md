# Sistema Flatpickr de CineTrack

## Objetivo

Flatpickr es el componente oficial utilizado para seleccionar fechas en CineTrack.

El campo visible deberá integrarse con el sistema global de formularios y percibirse como un input normal del proyecto, sin perder el comportamiento propio del selector de fecha.

---

## Alcance

Este sistema aplica a:

- Campos de fecha gestionados mediante Flatpickr.
- Contenedores asociados al campo.
- Iconos de calendario vinculados al control.
- Estados visuales del campo.
- Calendario emergente, únicamente en los aspectos mínimos definidos en este documento.

---

## Campo de fecha

El campo visible de Flatpickr deberá compartir con los demás inputs oficiales:

- Altura.
- Padding interno.
- Familia tipográfica.
- Tamaño de fuente.
- Peso tipográfico.
- Color del texto.
- Fondo.
- Borde.
- Radio.
- Alineación vertical.
- Transiciones visuales.

No deberá percibirse como un componente diferente al resto de los campos del formulario.

---

## Placeholder

El placeholder deberá respetar lo definido en:

- `docs/css/sistema-placeholders.md`

Flatpickr no deberá definir una variante propia de:

- Tipografía.
- Tamaño.
- Peso.
- Color.
- Opacidad.
- Altura de línea.

---

## Estados

El campo deberá tener estados visuales consistentes con los demás inputs.

### Normal

Deberá utilizar la apariencia base oficial de los campos del formulario.

### Hover

Podrá reforzar visualmente el borde, siempre de manera consistente con los demás inputs.

### Focus

Deberá utilizar el foco oficial del sistema de formularios.

El foco:

- No deberá cambiar la altura del campo.
- No deberá desplazar elementos.
- No deberá modificar el tamaño del borde de forma que altere el layout.
- Deberá ser visible y accesible.

### Disabled

Cuando exista, deberá comunicar claramente que el campo no está disponible.

No deberá perder legibilidad ni confundirse con un campo activo.

### Error

Cuando el campo tenga errores de validación, deberá utilizar el mismo sistema visual de errores que los demás inputs.

No deberá crear una variante de error exclusiva para Flatpickr.

---

## Icono de calendario

Cuando exista un icono:

- Deberá estar alineado verticalmente con el campo.
- No deberá alterar la altura del input.
- No deberá cubrir el texto.
- No deberá impedir la interacción con el campo.
- Deberá conservar una separación consistente respecto al contenido.

El icono podrá utilizar estilos de composición propios, pero no deberá provocar que Flatpickr se perciba como un control visualmente distinto.

---

## Calendario emergente

No se realizará un rediseño completo del calendario emergente.

Solo podrán normalizarse aspectos mínimos como:

- Familia tipográfica.
- Legibilidad del texto.
- Defectos visibles de alineación.
- Inconsistencias evidentes con la identidad visual del proyecto.

Deberán conservarse:

- La estructura del calendario.
- La navegación entre meses.
- La selección de fechas.
- Los estados propios de Flatpickr.
- El comportamiento responsive existente.
- La accesibilidad del componente.

---

## Formato y comportamiento

El sistema visual no deberá modificar:

- El formato actual de fecha.
- La configuración regional.
- La fecha enviada al formulario.
- La inicialización de Flatpickr.
- Las validaciones.
- La apertura del calendario.
- La selección de fechas.
- La carga de valores existentes durante la edición.

---

## Implementación

Los estilos deberán centralizarse principalmente en:

- `cinetrack/static/cinetrack/css/vendor/flatpickr-theme.css`

Podrán reutilizarse variables, tokens y reglas del sistema global de formularios.

Las páginas únicamente podrán conservar ajustes de composición cuando sean necesarios, por ejemplo:

- Distribución dentro del layout.
- Márgenes.
- Posición del icono.
- Ancho del contenedor.

No deberán definir individualmente:

- Altura.
- Tipografía.
- Tamaño de fuente.
- Color.
- Fondo.
- Borde.
- Radio.
- Estados hover o focus.
- Estilo del placeholder.

Se deberán eliminar reglas duplicadas o contradictorias siempre que sea posible.

---

## Fuera de alcance

Esta implementación no deberá modificar:

- Labels.
- Botones.
- Otros inputs.
- Modelos.
- Forms de Django.
- Views.
- Validaciones.
- Lógica de negocio.
- Estructura de los formularios.
- JavaScript funcional.