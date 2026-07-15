# Modelo de datos actual de CineTrack

## 1. Propósito y alcance

Este documento describe exclusivamente el modelo persistido actual de CineTrack: sus entidades, campos, relaciones, valores controlados, defaults, índices, restricciones y ordenamientos.

La descripción refleja los modelos Django vigentes. Las reglas de uso de la aplicación se distinguen de las restricciones que el esquema aplica directamente.

## 2. Visión general

### 2.1. Modelos persistidos

El modelo persistido actual está compuesto por tres modelos Django:

- `Contenido`, que representa una película o serie registrada;
- `SagaAlias`, que asocia una clave de saga calculada con un nombre personalizado;
- `Maraton`, que representa una colección personalizada de contenidos.

Todos utilizan una clave primaria `id` de tipo `BigAutoField`, generada implícitamente por Django.

### 2.2. Diagrama de relaciones

```text
SagaAlias
    Sin relación de base de datos con Contenido
    Asociación lógica mediante una clave calculada

Maraton N ───── N Contenido
    related_name: maratones
```

No existe una relación de base de datos entre `SagaAlias` y `Maraton`.

## 3. Contenido

### 3.1. Propósito actual

`Contenido` es la entidad central del modelo persistido actual. Reúne información descriptiva de una película o serie, su clasificación y el seguimiento personal registrado en CineTrack.

### 3.2. Campos

| Campo | Tipo Django | Configuración relevante | Descripción |
| --- | --- | --- | --- |
| `id` | `BigAutoField` | Clave primaria implícita | Identificador autogenerado |
| `titulo` | `CharField(max_length=200)` | Obligatorio | Título de la película o serie |
| `resumen` | `TextField` | `blank=True` | Descripción del contenido; admite valor vacío en la validación de Django |
| `imagen` | `URLField` | `blank=True`, `null=True` | URL del póster; puede almacenarse como `NULL` o valor vacío |
| `fecha` | `DateField` | `blank=True`, `null=True` | Fecha opcional utilizada para el estreno asociado al contenido |
| `tipo` | `CharField(max_length=10)` | Obligatorio; choices | Tipo de contenido |
| `plataforma` | `CharField(max_length=20)` | `blank=True`; choices | Plataforma asociada; admite valor vacío en la validación de Django |
| `calificacion` | `CharField(max_length=10)` | `blank=True`, `null=True`; choices | Calificación personal; puede almacenarse como `NULL` o valor vacío |
| `veces_vista` | `PositiveIntegerField` | Default explícito | Número de visualizaciones |
| `estado` | `CharField(max_length=20)` | Choices; default explícito | Estado de visualización |
| `volveria_a_ver` | `BooleanField` | Default explícito | Indica si el usuario volvería a ver el contenido |
| `tendra_continuacion` | `BooleanField` | Default explícito | Indica si se espera una continuación |
| `favorita` | `BooleanField` | Default explícito | Indica si el contenido está marcado como favorito |
| `fase_kanban` | `CharField(max_length=12)` | Choices; default explícito; indexado | Fase utilizada por el flujo de pendientes |
| `created_at` | `DateTimeField(auto_now_add=True)` | Automático | Fecha y hora de creación |
| `updated_at` | `DateTimeField(auto_now=True)` | Automático | Fecha y hora de la última modificación |

`blank=True` controla la validación de Django. `null=True` determina si la columna puede almacenar `NULL`; ambos conceptos no son equivalentes.

### 3.3. Defaults

| Campo | Default |
| --- | --- |
| `veces_vista` | `0` |
| `estado` | `pendiente` |
| `volveria_a_ver` | `False` |
| `tendra_continuacion` | `False` |
| `favorita` | `False` |
| `fase_kanban` | `nuevo` |

`created_at` se asigna al crear el registro y `updated_at` se actualiza automáticamente cuando Django guarda la instancia.

### 3.4. Valores controlados

Los campos siguientes utilizan `models.TextChoices`. Las tablas distinguen el valor almacenado de la etiqueta visible.

#### Tipo

| Valor almacenado | Etiqueta |
| --- | --- |
| `pelicula` | Película |
| `serie` | Serie |

#### Estado

| Valor almacenado | Etiqueta |
| --- | --- |
| `vista` | Vista |
| `pendiente` | Pendiente |

#### Plataforma

| Valor almacenado | Etiqueta |
| --- | --- |
| `prime` | Amazon Prime |
| `disney` | Disney+ |
| `hbo` | HBO |
| `netflix` | Netflix |
| `vix` | Vix |
| `otro` | Otra |

#### Calificación

| Valor almacenado | Etiqueta |
| --- | --- |
| `excelente` | Excelente |
| `buena` | Buena |
| `regular` | Regular |
| `mala` | Mala |
| `horrible` | Horrible |

#### Fase Kanban

| Valor almacenado | Etiqueta |
| --- | --- |
| `nuevo` | Nuevo |
| `pronto` | Pronto |
| `encurso` | En curso |
| `pausado` | Pausado |

### 3.5. Índices y restricciones

- `id` es la clave primaria.
- `fase_kanban` declara `db_index=True`.
- `veces_vista` utiliza `PositiveIntegerField` para representar una cantidad no negativa.
- No existe una restricción única sobre `titulo`.
- No existe una restricción única sobre la combinación de `titulo` y `plataforma`.
- No existen `UniqueConstraint` o `CheckConstraint` explícitas en `Meta`.
- Los choices participan en la validación de Django, pero no están declarados como `CheckConstraint` explícitas del modelo.

### 3.6. Ordenamiento

`Contenido` define:

```python
ordering = ["titulo"]
```

Las consultas que no especifican otro orden utilizan el título de forma ascendente.

## 4. SagaAlias

### 4.1. Propósito actual

`SagaAlias` almacena un nombre personalizado para una clave de saga generada por la lógica de agrupación de CineTrack.

### 4.2. Campos

| Campo | Tipo Django | Configuración relevante | Descripción |
| --- | --- | --- | --- |
| `id` | `BigAutoField` | Clave primaria implícita | Identificador autogenerado |
| `key` | `CharField(max_length=200)` | `unique=True`, `db_index=True` | Clave normalizada de saga |
| `nombre` | `CharField(max_length=200)` | Obligatorio | Nombre visible personalizado |

### 4.3. Unicidad e índice

`key` es único. Por tanto, una clave calculada puede tener como máximo un alias persistido.

El campo también declara `db_index=True`. La unicidad implica además una estructura de acceso única en la base de datos.

### 4.4. Asociación lógica con Contenido

Las sagas no se almacenan como una relación directa en `Contenido`. La aplicación calcula una clave normalizada desde el título y utiliza esa clave para localizar un `SagaAlias`.

No existen un modelo `Saga`, una foreign key o una relación many-to-many entre `SagaAlias` y `Contenido`.

### 4.5. Ordenamiento

`SagaAlias` define:

```python
ordering = ["nombre"]
```

## 5. Maraton

### 5.1. Propósito actual

`Maraton` representa una colección personalizada de contenidos audiovisuales.

### 5.2. Campos

| Campo | Tipo Django | Configuración relevante | Descripción |
| --- | --- | --- | --- |
| `id` | `BigAutoField` | Clave primaria implícita | Identificador autogenerado |
| `nombre` | `CharField(max_length=200)` | `unique=True` | Nombre de la colección |
| `descripcion` | `TextField` | `blank=True` | Descripción; admite valor vacío en la validación de Django |
| `contenidos` | `ManyToManyField(Contenido)` | `blank=True`, `related_name="maratones"` | Contenidos incluidos en la colección |
| `created_at` | `DateTimeField(auto_now_add=True)` | Automático | Fecha y hora de creación |
| `updated_at` | `DateTimeField(auto_now=True)` | Automático | Fecha y hora de la última modificación |

### 5.3. Relación con Contenido

La relación entre `Maraton` y `Contenido` es de muchos a muchos:

- un maratón puede contener múltiples contenidos;
- un contenido puede pertenecer a múltiples maratones.

Django administra una tabla intermedia implícita. No existe un modelo intermedio explícito con atributos adicionales.

### 5.4. Relación inversa

El `related_name` de la relación es `maratones`. Desde una instancia de `Contenido`, la relación inversa se consulta mediante:

```python
contenido.maratones.all()
```

### 5.5. Restricciones

- `id` es la clave primaria.
- `nombre` es único.
- La relación permite una colección vacía en formularios y validación de Django mediante `blank=True`.
- La tabla intermedia administrada por Django identifica cada asociación entre un maratón y un contenido.
- No existen constraints adicionales declaradas en `Meta`.

### 5.6. Ordenamiento

`Maraton` define:

```python
ordering = ["nombre"]
```

## 6. Reglas de integridad y límites actuales

### 6.1. Reglas representadas por tipos y defaults

El modelo representa directamente las siguientes reglas:

- identificadores autogenerados para los tres modelos;
- número de visualizaciones no negativo mediante `PositiveIntegerField`;
- estado inicial `pendiente`;
- fase inicial `nuevo`;
- indicadores booleanos inicialmente en `False`;
- unicidad de `SagaAlias.key`;
- unicidad de `Maraton.nombre`;
- relación many-to-many entre maratones y contenidos;
- fechas automáticas de creación y actualización.

### 6.2. Reglas no expresadas como constraints

El esquema no declara constraints para garantizar que:

- solo los contenidos pendientes utilicen una fase Kanban;
- un contenido visto tenga una calificación;
- `volveria_a_ver` se utilice exclusivamente con contenidos vistos;
- la combinación de título y plataforma sea única;
- los valores de choices se validen mediante `CheckConstraint` explícitas.

Estas condiciones pueden ser aplicadas por formularios o vistas, pero no constituyen restricciones cruzadas del modelo actual.

### 6.3. Alcance del modelo implementado

Los registros actuales no están asociados mediante una relación de propiedad con un usuario. `Contenido` tampoco persiste un identificador externo de TMDB.

Este documento se limita al esquema implementado y no define entidades adicionales.

