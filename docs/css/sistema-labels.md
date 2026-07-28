# Sistema de labels de CineTrack

## Uso

Las labels representan el nombre o descripción de un campo de formulario o control de interfaz.

Deben mantener una identidad visual única en todo el proyecto.

---

## Tipografía

Las labels utilizan la tipografía oficial de interfaz definida en:

- `docs/css/sistema-tipografico-global.md`

Fuente:

- Teko

---

## Aplicaciones

Este sistema aplica a:

- Formularios.
- Filtros.
- Búsquedas.
- Switches.
- Componentes reutilizables.
- Includes.
- Modales.
- Cualquier label equivalente.

---

## No aplica a

No forman parte de este sistema:

- Estadísticas.
- Valores mostrados al usuario.
- Texto de tarjetas.
- Contenido de tablas.
- Información descriptiva.
- Texto dinámico.
- Cualquier contenido que no identifique un campo de interfaz.

Estos elementos deberán seguir utilizando la tipografía correspondiente definida en el sistema tipográfico.

---

# Especificación de implementación

Todas las labels deberán compartir un único estilo global.

Ese estilo únicamente podrá definir:

- Familia tipográfica.
- Tamaño.
- Peso.
- Color.
- Transformación a mayúsculas.
- Espaciado entre letras.

Las páginas únicamente podrán modificar aspectos de composición, por ejemplo:

- Márgenes.
- Separación respecto al campo.
- Distribución del layout.

No deberán modificar:

- Tipografía.
- Tamaño.
- Peso.
- Color.
- Estilo visual.

El sistema deberá centralizarse utilizando la clase global correspondiente (por ejemplo `.form-label`) o la solución que mejor se adapte a la arquitectura del proyecto.

No deberán existir variantes visuales adicionales de labels.