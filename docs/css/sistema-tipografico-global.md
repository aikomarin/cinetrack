# Sistema tipográfico definitivo de CineTrack

## 1. Bebas Neue

### Uso exclusivo

Es la fuente de identidad del proyecto.

Debe utilizarse únicamente en elementos de alto impacto visual.

### Aplicaciones

* Logo CineTrack.
* Hero principal.
* Títulos principales de página.
* Encabezados especiales.
* Títulos destacados (como Detalle).
* Elementos de branding.

### No utilizar en

* Labels.
* Botones.
* Formularios.
* Párrafos.
* Placeholders.
* Mensajes.
* Badges.

---

## 2. Teko

### Fuente de interfaz

Su función es estructurar la interfaz, no mostrar contenido.

### Aplicaciones

* Labels de formularios.
* Subtítulos.
* Títulos de sección.
* Navegación.
* Paginación.
* Encabezados internos.

### No utilizar en

* Texto escrito por el usuario.
* Placeholders.
* Inputs.
* Textareas.
* Botones.
* Mensajes.
* Badges.
* Estadísticas.

---

## 3. DM Sans

### Fuente de contenido

Debe convertirse en la fuente predominante del proyecto.

Todo aquello que el usuario:

* escribe;
* lee;
* interpreta;
* compara;

debe utilizar **DM Sans**.

### Aplicaciones

#### Formularios

* Texto escrito en inputs.
* Números.
* Textareas.
* Fecha.
* Placeholders.
* Opciones de selects.
* Valor visible de los selects.

#### Componentes

* Botones.
* Badges.
* Chips.
* Mensajes.
* Tarjetas.
* Estadísticas.
* Estados vacíos.
* Filtros.
* Metadatos.
* Descripciones.
* Resúmenes.

---

## Excepción aprobada

La única combinación tipográfica aprobada es el encabezado de **Registrar** y **Editar**.

**REGISTRAR** | **PELÍCULA O SERIE**

* **REGISTRAR** → Bebas Neue.
* **PELÍCULA O SERIE** → Teko.

Esta composición forma parte de la identidad visual de CineTrack y debe mantenerse sin modificaciones.

---

# # Especificación de implementación

Los siguientes cambios son obligatorios para que CineTrack cumpla con el sistema tipográfico definido en este documento. Cualquier modificación futura deberá respetar estas reglas, salvo que este documento sea actualizado.

## 1. Normalizar los placeholders

Todos los placeholders deben utilizar **DM Sans**.

No debe utilizarse **Teko** para ningún placeholder del proyecto.

---

## 2. Unificar la tipografía de los selects

Actualmente existe una inconsistencia:

* Select cerrado → **Teko**.
* Select desplegado → **DM Sans**.

Estado definitivo:

* Select cerrado → **DM Sans**.
* Select desplegado → **DM Sans**.

---

## 3. Unificar el texto escrito por el usuario

Todo el texto escrito por el usuario debe utilizar **DM Sans**, incluyendo:

* Inputs.
* Campo de fecha.
* Campos numéricos.
* Textareas.
* Valor visible de los selects.

---

## 4. Unificar los botones

Todos los botones del proyecto deben utilizar **DM Sans**, sin excepciones.

Incluye:

* Primarios.
* Primarios con glow.
* Secundarios.
* Ghost.
* Danger.
* Botones pequeños.
* Botones con icono.

---

## 5. Unificar badges y chips

Todos los badges y chips del proyecto deben utilizar **DM Sans**.

---

## 6. Unificar mensajes del sistema

Todos los mensajes deben utilizar **DM Sans**, incluyendo:

* Error.
* Éxito.
* Advertencia.
* Información.
* Validaciones de formularios.