# Sistema de Títulos

## Objetivo

Definir la jerarquía oficial de títulos utilizada en CineTrack para mantener una identidad visual consistente, facilitar la reutilización de componentes y evitar la creación de nuevas variantes tipográficas innecesarias.

Este documento complementa el **Sistema Tipográfico Global**. Aquí no se definen fuentes, sino **cuándo utilizar cada nivel de título**.

---

# Alcance

Aplica a todas las pantallas desarrolladas actualmente en CineTrack:

- Home
- Buscar
- Catálogo
- Registrar
- Editar
- Detalle
- Favoritos
- Pendientes
- Volvería a ver
- Maratones

No documenta componentes específicos como:

- Dashboard
- Podios
- Actividad reciente
- Tarjetas especiales
- Componentes internos del Kanban

Estos componentes podrán tener documentación propia cuando sea necesario.

---

# Jerarquía oficial

Actualmente CineTrack utiliza **seis niveles oficiales de títulos**.

---

# Nivel 1 — Hero principal

Es el título más importante de una pantalla.

Se utiliza únicamente cuando la pantalla posee un encabezado tipo Hero.

## Ejemplos

- CATÁLOGO REGISTRADO
- BUSCAR PELÍCULA O SERIE
- MARATONES
- Nombre de una saga
- Nombre de un maratón

## Características

- Fuente de marca (Bebas Neue).
- Gran tamaño.
- Máxima jerarquía visual.
- Siempre ubicado dentro del Hero.

---

# Nivel 2 — Título principal de página

Corresponde a pantallas que utilizan el componente **Page Shell**.

No reemplaza al Hero.

## Ejemplos

- Registrar contenido
- Editar contenido
- Favoritos
- Pendientes
- Volvería a ver
- Crear maratón

## Características

- Fuente de marca (Bebas Neue).
- Menor tamaño que el Hero.
- Puede incorporar:
  - icono;
  - subtítulo;
  - información contextual.

---

# Nivel 3 — Subtítulos

Se utilizan para complementar un título principal.

Nunca sustituyen al título.

## Ejemplos

- EXPLORA TU COLECCIÓN POR TIPO, PLATAFORMA Y ESTADO.
- Tipo de contenido mostrado junto al título de Registrar o Editar.
- Información contextual del Page Shell.

## Características

- Tipografía Teko.
- Color secundario.
- Siempre subordinados al título principal.
- No deben competir visualmente con el encabezado.

---

# Nivel 4 — Títulos de sección

Dividen una pantalla en bloques funcionales.

Cada sección importante debe comenzar con uno de estos encabezados.

## Ejemplos

- INFORMACIÓN DEL CONTENIDO
- INFORMACIÓN DE VISIONADO
- RESULTADOS
- TOP 5
- PELÍCULAS
- SERIES

## Características

- Tipografía Teko.
- Mayúsculas.
- Alto peso tipográfico.
- Separación clara respecto al contenido.
- Pueden incorporar líneas decorativas o iconos cuando el componente lo requiera.

---

# Nivel 5 — Títulos de contenido

Corresponden al nombre de un contenido audiovisual.

## Ejemplos

- 3 Idiotas
- Castle
- Breaking Bad
- Bones

## Características

- Tipografía DM Sans.
- Deben priorizar la legibilidad.
- Admiten truncado o límite de líneas cuando el componente lo requiera.
- No utilizan mayúsculas forzadas.

---

# Nivel 6 — Encabezados de modales

Se utilizan únicamente como título principal de un diálogo modal.

## Ejemplos

- Confirmar eliminación

## Características

- Tipografía Teko.
- Alto contraste.
- Jerarquía suficiente para identificar rápidamente la acción del modal.
- Puede acompañarse de un icono.

---

# Reglas generales

## Una sola jerarquía

Cada pantalla debe seguir la jerarquía establecida.

No deben aparecer dos títulos principales compitiendo visualmente.

---

## No crear variantes nuevas

Antes de crear un nuevo estilo de título debe verificarse si alguno de los niveles existentes cubre la necesidad.

Si un nuevo caso realmente requiere otra jerarquía, deberá documentarse primero en este Design System.

---

## Consistencia tipográfica

Cada nivel utiliza siempre la tipografía correspondiente definida en el **Sistema Tipográfico Global**.

No deben modificarse manualmente:

- familia tipográfica;
- peso;
- tamaño;
- espaciados;
- color.

Las pantallas únicamente pueden ajustar distribución o separación cuando el layout lo requiera.

---

## Componentes especializados

Algunos componentes reutilizables podrán tener pequeñas adaptaciones internas (por ejemplo, truncado o límite de líneas), pero deberán seguir perteneciendo a uno de los niveles definidos en este documento.

---

# Referencias

Este sistema depende de:

- Sistema Tipográfico Global
- Sistema de Labels
- Design Tokens

---

# Implementación

Actualmente la jerarquía se implementa mediante los siguientes componentes:

| Nivel | Implementación principal |
|--------|--------------------------|
| Hero principal | `.hero-title` |
| Título principal de página | `.page-shell-title` |
| Subtítulos | `.hero-sub`, subtítulos de `page-shell` |
| Títulos de sección | `.section-title`, `.content-form-section-title`, `.favorites-section-title` |
| Títulos de contenido | `.top-card-name` |
| Encabezados de modal | `.confirmation-modal-title` |

La implementación podrá refactorizarse en el futuro, pero la jerarquía visual deberá mantenerse.

---

# Fuera de alcance

Este documento no define:

- tamaños tipográficos;
- familias tipográficas;
- pesos;
- colores;
- line-height;
- letter-spacing;
- componentes específicos como Dashboard, Podios o Kanban.

Estos aspectos se documentan en sus respectivos sistemas.