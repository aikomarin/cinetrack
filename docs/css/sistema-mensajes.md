# Sistema de Mensajes Globales de CineTrack

## Objetivo

Los mensajes globales comunican el resultado de una acción completada por el usuario.

Todos los mensajes deberán compartir una única identidad visual y un comportamiento consistente en todo el proyecto.

---

## Alcance

Este sistema aplica exclusivamente a los mensajes globales mostrados mediante el sistema oficial de mensajes de Django.

Incluye las siguientes categorías:

- Éxito.
- Error.
- Advertencia.
- Información.

No aplica a:

- Errores inline de formularios.
- Errores de validación de campos.
- Confirmaciones dentro de modales.
- Diálogos de confirmación.
- Estados vacíos.
- Indicadores de carga.
- Notificaciones propias de JavaScript.

---

## Tipografía

La tipografía deberá respetar lo definido en:

- `docs/css/sistema-tipografico-global.md`

---

# Especificación visual

Todos los mensajes deberán compartir:

- Padding.
- Radio.
- Borde.
- Separación interna.
- Separación respecto al contenido.
- Tipografía.
- Tamaño del texto.
- Peso tipográfico.
- Iconografía.
- Botón de cierre.
- Transiciones.

No deberán existir variantes estructurales entre categorías.

Únicamente cambiarán:

- Color principal.
- Color del borde.
- Color del fondo.
- Icono.

---

## Categorías oficiales

### Éxito

Se utilizará cuando una operación termine correctamente.

Ejemplos:

- Crear.
- Guardar.
- Actualizar.
- Eliminar.
- Registrar.

---

### Error

Se utilizará cuando una operación no pueda completarse.

No deberá utilizarse para errores de validación de campos.

---

### Advertencia

Se utilizará cuando el usuario deba prestar atención a una situación que no constituye un error.

Ejemplos:

- Contenido duplicado.
- Acción parcialmente completada.
- Operación no recomendada.

---

### Información

Se utilizará para comunicar información relevante que no implique éxito, error o advertencia.

---

## Iconografía

Cada categoría utilizará un único icono oficial.

Los iconos deberán formar parte del componente.

No deberán incluirse emojis directamente dentro de los textos.

---

## Botón de cierre

Todos los mensajes deberán incluir un único botón de cierre consistente.

El botón deberá mantener la misma apariencia en todas las categorías.

---

## Accesibilidad

Los mensajes deberán utilizar la semántica adecuada según su propósito.

Deberán incorporar:

- `role="status"` cuando comuniquen información no crítica.
- `role="alert"` cuando comuniquen errores o advertencias que requieran atención inmediata.

---

## Implementación

Los mensajes globales deberán renderizarse mediante un único componente reutilizable.

Las categorías deberán diferenciarse únicamente mediante modificadores del componente.

No deberán depender directamente de las clases visuales predeterminadas de Bootstrap.

El sistema deberá centralizar:

- Geometría.
- Tipografía.
- Iconografía.
- Estados.
- Colores.
- Espaciado.

Se deberán eliminar reglas duplicadas siempre que sea posible.

---

## Comportamiento

Los mensajes deberán mantener el comportamiento actual del proyecto.

Esta implementación no deberá modificar:

- El sistema Django Messages.
- El flujo de generación de mensajes.
- La lógica de las vistas.
- El momento en que aparecen.
- El cierre manual mediante el botón correspondiente.

La desaparición automática, si llegara a implementarse, deberá documentarse como una mejora independiente.

---

## Fuera de alcance

Esta implementación no deberá modificar:

- Errores inline de formularios.
- Validaciones.
- Modales de confirmación.
- Botones.
- Formularios.
- JavaScript.
- Models.
- Forms.
- Views.