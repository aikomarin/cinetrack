# Sistema de placeholders de CineTrack

## Uso

Los placeholders sirven como texto de apoyo dentro de los campos de formulario.

Su función es orientar al usuario sobre el tipo de información que puede ingresar o seleccionar, sin sustituir a la label del campo.

---

## Tipografía

Los placeholders utilizan la tipografía oficial de contenido definida en:

- `docs/css/sistema-tipografico-global.md`

Fuente:

- DM Sans

---

## Aplicaciones

Este sistema aplica a:

- Inputs de texto.
- Inputs numéricos.
- Campos de búsqueda.
- Textareas.
- Selects.
- Selectores personalizados.
- Campos de fecha.
- Cualquier control equivalente que muestre texto de ayuda dentro del campo.

---

## Reglas de contenido

Los placeholders deberán:

- Ser breves.
- Ser claros.
- Describir el contenido esperado.
- Mantener una redacción consistente.
- Utilizar mayúscula inicial únicamente cuando corresponda.
- Evitar signos innecesarios.
- Evitar repetir exactamente el texto de la label cuando no aporte información adicional.

Ejemplos válidos:

- `Escribe un título`
- `Selecciona un tipo`
- `Sin plataforma`
- `Sin calificación`
- `dd/mm/aaaa`

---

## No utilizar para

Los placeholders no deberán utilizarse como sustituto de:

- Labels.
- Mensajes de validación.
- Instrucciones extensas.
- Texto de ayuda permanente.
- Valores predeterminados.
- Información obligatoria para comprender el campo.

---

# Especificación visual

Todos los placeholders deberán compartir una identidad visual consistente.

El estilo global deberá definir:

- Familia tipográfica.
- Tamaño.
- Peso.
- Color.
- Opacidad.
- Altura de línea.

Las páginas o componentes no deberán modificar de forma individual:

- Tipografía.
- Tamaño.
- Peso.
- Color.
- Opacidad.
- Estilo visual.

Únicamente podrán realizar ajustes de composición cuando sean necesarios para el funcionamiento del control.

---

# Selects y selectores personalizados

El texto equivalente a placeholder dentro de selects o selectores personalizados deberá utilizar el mismo sistema visual.

Esto incluye textos como:

- `Selecciona un tipo`
- `Sin plataforma`
- `Sin calificación`

El estado de placeholder deberá distinguirse del valor seleccionado sin utilizar una tipografía distinta.

---

# Flatpickr

El placeholder de los campos gestionados mediante Flatpickr deberá respetar este sistema.

La apariencia general del componente Flatpickr se documentará por separado en:

- `docs/css/sistema-flatpickr.md`

---

# Especificación de implementación

El sistema deberá centralizarse en las reglas globales correspondientes, incluyendo cuando aplique:

- `::placeholder`
- Selects.
- Selectores personalizados.
- Flatpickr.
- Controles de Bootstrap.

Se deberán eliminar reglas duplicadas siempre que sea posible.

No deberán modificarse:

- La estructura de los formularios.
- La lógica de los campos.
- Las validaciones.
- JavaScript.
- El tamaño de los inputs.
- Labels.
- Botones.
- El comportamiento funcional de los controles.