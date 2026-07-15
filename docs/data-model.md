# Modelo de datos de CineTrack

## Descripción general

CineTrack utiliza un modelo de datos centrado en la entidad `Contenido`, que representa las películas y series registradas en la aplicación.

El diseño busca mantener una estructura simple para el catálogo audiovisual, incorporando en una misma entidad la información descriptiva del contenido, su clasificación y el seguimiento personal realizado por el usuario.

Actualmente, el dominio está compuesto por tres modelos principales:

- `Contenido`
- `SagaAlias`
- `Maraton`

---

## Contenido

`Contenido` es la entidad principal del dominio y representa una película o serie almacenada en el catálogo.

La información se organiza conceptualmente en cinco grupos.

### Datos principales

| Campo | Descripción |
| --- | --- |
| `titulo` | Nombre de la película o serie |
| `resumen` | Descripción del contenido |
| `imagen` | URL de la imagen o póster |
| `fecha` | Fecha asociada al estreno del contenido |

### Clasificación

| Campo | Descripción |
| --- | --- |
| `tipo` | Clasifica el contenido como película o serie |
| `plataforma` | Plataforma de streaming asociada |
| `calificacion` | Valoración personal del contenido |

### Seguimiento y preferencias

| Campo | Descripción |
| --- | --- |
| `veces_vista` | Número de veces que el contenido ha sido visto |
| `estado` | Indica si el contenido fue visto o continúa pendiente |
| `volveria_a_ver` | Indica si el usuario volvería a consumir el contenido |
| `tendra_continuacion` | Registra si se espera una continuación |
| `favorita` | Identifica contenidos marcados como favoritos |

### Flujo Kanban

El campo `fase_kanban` representa la posición de un contenido pendiente dentro del flujo de intención de visualización.

Las fases disponibles son:

- Nuevo
- Pronto
- En curso
- Pausado

### Metadatos

`created_at` y `updated_at` registran automáticamente la fecha de creación y la última modificación de cada contenido.

---

## SagaAlias

`SagaAlias` almacena nombres personalizados para las claves de saga generadas por la lógica de agrupación de CineTrack.

Las sagas no se almacenan como una relación directa dentro de `Contenido`. La aplicación calcula dinámicamente una clave normalizada a partir del título del contenido.

`SagaAlias` permite asociar esa clave con un nombre de presentación definido por el usuario.

Esta estrategia permite conservar la agrupación automática sin requerir una entidad `Saga` ni una relación adicional en el modelo principal.

---

## Maraton

`Maraton` representa una colección personalizada de contenidos audiovisuales.

Cada maratón contiene:

- un nombre único;
- una descripción opcional;
- una colección de contenidos;
- metadatos de creación y actualización.

La relación entre `Maraton` y `Contenido` es de muchos a muchos.

Un maratón puede contener múltiples películas o series y un mismo contenido puede formar parte de diferentes maratones.

La relación se implementa mediante ManyToManyField debido a que actualmente no existen atributos adicionales asociados a la pertenencia de un contenido dentro de un maratón.

```text
Maraton N ───── N Contenido