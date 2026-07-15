# API REST de CineTrack

## 1. Propósito y estado actual

CineTrack expone una API REST construida con Django REST Framework. La API actual permite consultar el recurso `Contenido` y no ofrece operaciones de escritura.

El acceso es público: no se exige autenticación para listar o consultar contenidos.

## 2. Ruta base y enrutamiento

La API forma parte del enrutamiento de la aplicación Django bajo el prefijo:

```text
/cinetrack/api/
```

### 2.1. Raíz de la API

`DefaultRouter` genera una raíz navegable:

```text
/cinetrack/api/
```

Esta ruta permite descubrir el recurso `contenidos` registrado en el router.

### 2.2. Recurso contenidos

El recurso principal se encuentra en:

```text
/cinetrack/api/contenidos/
```

El router utiliza `contenido` como basename interno para generar los nombres de las rutas de lista y detalle.

### 2.3. Sufijos de formato

El `DefaultRouter` también admite variantes con sufijo de formato. Por ejemplo:

```text
/cinetrack/api/contenidos.json
/cinetrack/api/contenidos/1.json
```

Las rutas con slash final son la forma canónica documentada por CineTrack.

## 3. Endpoints

### 3.1. Raíz

```text
/cinetrack/api/
```

Devuelve los recursos registrados en el router. Actualmente contiene un enlace al listado de contenidos.

### 3.2. Lista de contenidos

```text
/cinetrack/api/contenidos/
```

Devuelve la colección completa de contenidos serializados.

Nombre de ruta generado por el router:

```text
contenido-list
```

### 3.3. Detalle de contenido

```text
/cinetrack/api/contenidos/{id}/
```

Devuelve un contenido individual identificado por su clave primaria.

Nombre de ruta generado por el router:

```text
contenido-detail
```

## 4. Métodos HTTP

| Endpoint | `GET` | `HEAD` | `OPTIONS` | `POST` | `PUT` | `PATCH` | `DELETE` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `/cinetrack/api/` | Sí | Sí | Sí | No | No | No | No |
| `/cinetrack/api/contenidos/` | Sí | Sí | Sí | No | No | No | No |
| `/cinetrack/api/contenidos/{id}/` | Sí | Sí | Sí | No | No | No | No |

`GET` permite listar o recuperar recursos. `HEAD` devuelve los encabezados correspondientes y `OPTIONS` describe las operaciones admitidas por DRF.

Las operaciones de creación, actualización parcial, actualización completa y eliminación no están expuestas.

## 5. Representación de Contenido

### 5.1. Campos expuestos

`ContenidoSerializer` declara explícitamente los siguientes campos:

| Campo | Descripción |
| --- | --- |
| `id` | Identificador del contenido |
| `titulo` | Título de la película o serie |
| `resumen` | Descripción del contenido |
| `imagen` | URL del póster o imagen |
| `fecha` | Fecha asociada al estreno |
| `tipo` | Valor interno del tipo de contenido |
| `plataforma` | Valor interno de la plataforma |
| `calificacion` | Valor interno de la calificación personal |
| `veces_vista` | Número de visualizaciones |
| `estado` | Valor interno del estado de visualización |
| `volveria_a_ver` | Indica si el usuario volvería a ver el contenido |
| `tendra_continuacion` | Indica si se espera una continuación |
| `favorita` | Indica si el contenido está marcado como favorito |
| `fase_kanban` | Valor interno de la fase de pendientes |
| `created_at` | Fecha y hora de creación |
| `updated_at` | Fecha y hora de la última actualización |

Los campos basados en choices se representan mediante sus valores internos, no mediante sus etiquetas visibles.

### 5.2. Campos declarados como solo lectura

El serializer declara expresamente como campos de solo lectura:

- `id`;
- `created_at`;
- `updated_at`.

### 5.3. Comportamiento efectivo de solo lectura

Aunque el serializer solo marca esos tres campos mediante `read_only_fields`, todos los campos son efectivamente de solo lectura en la API actual.

`ContenidoViewSet` hereda de `ReadOnlyModelViewSet`, por lo que no expone acciones para crear, actualizar o eliminar contenidos.

## 6. Ejemplo de respuesta JSON

Los valores siguientes son representativos y respetan la estructura definida por el serializer. No corresponden a un registro extraído de producción.

### 6.1. Respuesta de lista

El endpoint de lista devuelve directamente un array JSON:

```json
[
  {
    "id": 1,
    "titulo": "Ejemplo de película",
    "resumen": "Resumen representativo del contenido.",
    "imagen": "https://image.tmdb.org/t/p/w500/example.jpg",
    "fecha": "2024-01-15",
    "tipo": "pelicula",
    "plataforma": "netflix",
    "calificacion": "buena",
    "veces_vista": 1,
    "estado": "vista",
    "volveria_a_ver": true,
    "tendra_continuacion": false,
    "favorita": true,
    "fase_kanban": "nuevo",
    "created_at": "2026-07-15T12:00:00-06:00",
    "updated_at": "2026-07-15T12:00:00-06:00"
  }
]
```

La respuesta no contiene una envoltura con campos como `count`, `next` o `results` porque la API no tiene paginación configurada.

### 6.2. Colección vacía

Cuando no existen contenidos, la respuesta es:

```json
[]
```

## 7. Autenticación y permisos

### 7.1. Autenticación disponible

El proyecto no define una configuración `REST_FRAMEWORK` propia ni clases de autenticación específicas en el ViewSet. Se aplican las clases predeterminadas de DRF:

- `SessionAuthentication`;
- `BasicAuthentication`.

Estas clases permiten que DRF reconozca una sesión Django o credenciales HTTP Basic, pero la API actual no exige que el cliente se autentique.

### 7.2. Acceso público

El permiso predeterminado efectivo es `AllowAny`. Cualquier cliente puede consultar los endpoints sin iniciar sesión.

No existe configuración de tokens, JWT, API keys, permisos por usuario o comprobaciones de propiedad para este recurso.

## 8. Comportamiento de las colecciones

### 8.1. Ordenamiento

El ViewSet utiliza `Contenido.objects.all()`. El modelo `Contenido` define ordenamiento predeterminado por `titulo`, por lo que la lista se devuelve actualmente en ese orden.

La API no permite seleccionar otro orden mediante parámetros de consulta.

### 8.2. Paginación

No existe una clase de paginación ni un tamaño de página configurados. El endpoint de lista devuelve todos los contenidos en un único array.

### 8.3. Filtros y búsqueda

No existen filter backends, campos de búsqueda ni filtros REST configurados. Los filtros disponibles en el catálogo HTML no se aplican a la API.

## 9. Límites y capacidades no configuradas

### 9.1. Throttling

No existen clases ni tasas de throttling configuradas. La API no impone actualmente límites de solicitudes mediante DRF.

### 9.2. Versionado

No existe una clase de versionado configurada. La ruta no incluye una versión y la API no utiliza versionado por encabezado o parámetro de consulta.

### 9.3. Recursos no expuestos

La API no expone recursos REST independientes para:

- `SagaAlias`;
- `Maraton`;
- dashboard;
- fases Kanban;
- favoritos;
- búsquedas en TMDB.

## 10. Referencias al código

El contrato actual se implementa en:

- [`config/urls.py`](../config/urls.py), que incorpora las rutas de la aplicación bajo `/cinetrack/`;
- [`cinetrack/urls.py`](../cinetrack/urls.py), que registra el router bajo `/api/`;
- [`cinetrack/serializers.py`](../cinetrack/serializers.py), que define `ContenidoSerializer`;
- [`cinetrack/views.py`](../cinetrack/views.py), que define `ContenidoViewSet`.

