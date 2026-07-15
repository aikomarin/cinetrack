# Arquitectura de CineTrack

## 1. Propósito y alcance

Este documento presenta la organización general de CineTrack, las responsabilidades de sus componentes y los flujos principales de la aplicación actual.

El detalle de las entidades persistidas se encuentra en el [modelo de datos](../data-model.md). El comportamiento específico de la fuente externa utilizada por CineTrack se documenta en la [integración con TMDB](../integrations/tmdb.md). Las razones que motivaron elecciones concretas se mantienen en las [decisiones técnicas](../technical-decisions.md).

Este overview describe exclusivamente el sistema implementado. No define funcionalidades futuras ni sustituye la documentación especializada.

## 2. Visión general del sistema

CineTrack es una aplicación web monolítica construida con Django. La aplicación ofrece una interfaz HTML renderizada mediante templates de Django y una API REST construida con Django REST Framework.

Los datos se almacenan en PostgreSQL mediante el ORM de Django. Para la búsqueda externa de películas y series, CineTrack consulta TMDB y normaliza sus respuestas antes de utilizarlas en la aplicación.

```text
Navegador
   |
   +-- Interfaz HTML
   |
   +-- API REST de solo lectura
            |
            v
          Django
            |
            +-- ORM de Django --> PostgreSQL
            |
            +-- Integración externa --> TMDB
```

## 3. Componentes y responsabilidades

### Configuración del proyecto

El paquete `config` contiene la configuración de Django, el enrutamiento principal y los puntos de entrada WSGI y ASGI.

### Aplicación CineTrack

La aplicación `cinetrack` concentra el comportamiento actual del producto:

- los modelos representan la información persistida;
- los formularios reciben y validan los datos de la interfaz web;
- las vistas coordinan las solicitudes, consultas, mutaciones y respuestas;
- los templates generan la interfaz HTML;
- los archivos estáticos proporcionan estilos y comportamiento en el navegador;
- los serializers y el ViewSet exponen el recurso REST actual.

Parte de las reglas y transformaciones reutilizadas por distintas vistas se encuentra actualmente en funciones auxiliares de `utils.py`. Entre ellas se encuentran la agrupación de sagas y el acceso a TMDB.

### Interfaces

Las vistas HTML y la API REST operan sobre la misma aplicación y persistencia. Las operaciones de escritura se realizan actualmente mediante los flujos de la interfaz web; la API expuesta es pública y de solo lectura.

## 4. Interfaces y enrutamiento

`config/urls.py` define el enrutamiento raíz del proyecto. La ruta principal redirige a la interfaz de CineTrack, el administrador de Django se expone bajo `/admin/` y las rutas de la aplicación se delegan a `cinetrack/urls.py` bajo el prefijo `/cinetrack/`.

Las rutas de la interfaz web se agrupan por las funcionalidades actuales, entre ellas dashboard, catálogo, contenidos, búsqueda, sagas, pendientes, favoritos y maratones.

La API REST se incorpora al mismo enrutamiento mediante un `DefaultRouter` de Django REST Framework. Actualmente expone `Contenido` mediante `ContenidoViewSet`, implementado como `ReadOnlyModelViewSet`.

La API utiliza el prefijo `/cinetrack/api/`. Sus endpoints, métodos, campos, permisos y capacidades actuales se documentan en [API REST de CineTrack](../api.md).

## 5. Flujos principales

### 5.1. Consulta del dashboard

La vista principal consulta el conjunto de contenidos y construye una proyección de lectura para `home.html`. El contexto incluye indicadores generales, distribución por plataforma, progreso de visualización, actividad reciente y selecciones de contenidos destacados.

### 5.2. Consulta del catálogo

El catálogo recibe filtros desde la solicitud, los aplica al conjunto de `Contenido` y organiza los resultados para su presentación. Cuando varios contenidos comparten una clave de saga, se muestran como una agrupación; los demás se presentan individualmente.

La paginación se aplica después de construir los grupos. De este modo, una saga se conserva como una unidad visual dentro del catálogo.

La pertenencia a una saga se deriva actualmente del título. `SagaAlias` permite personalizar el nombre visible de una agrupación sin establecer una relación directa desde `Contenido`.

### 5.3. Búsqueda y registro desde TMDB

CineTrack utiliza TMDB como fuente externa para localizar películas y series antes de registrarlas en el catálogo local.

```text
Consulta del usuario
        |
        v
Vista de búsqueda
        |
        v
Integración con TMDB
        |
        v
Resultados normalizados
        |
        v
Selección del usuario
        |
        v
Registro local como Contenido
```

La vista delega la comunicación externa y recibe una representación común para películas y series. El usuario selecciona uno de esos resultados y la aplicación lo convierte en un registro local.

Los recursos consultados, la normalización y el manejo de errores externos se describen en la [integración con TMDB](../integrations/tmdb.md).

### 5.4. Gestión de maratones

La gestión de maratones utiliza vistas y formularios de Django para trabajar con colecciones personalizadas de contenidos. Los flujos web permiten consultar y administrar maratones y su selección de contenidos.

La relación persistida entre `Maraton` y `Contenido` se documenta en el [modelo de datos](../data-model.md).

## 6. Persistencia

CineTrack utiliza PostgreSQL como base de datos y accede a la información mediante el ORM de Django. La configuración admite una URL de conexión completa o variables individuales para la conexión local.

Las entidades, campos, relaciones, valores controlados y restricciones actuales se describen en el [modelo de datos](../data-model.md).

## 7. Integraciones externas

TMDB es la única integración externa documentada actualmente. Se utiliza como fuente de metadatos durante la búsqueda de películas y series.

La aplicación adapta las diferencias entre los resultados externos antes de entregarlos a las vistas. Los detalles del flujo HTTP, la normalización, las imágenes, las fechas, los errores y la configuración se encuentran en la [documentación de TMDB](../integrations/tmdb.md).

## 8. Decisiones arquitectónicas relacionadas

Las siguientes decisiones explican elecciones relevantes para la arquitectura actual:

- contrato explícito de serialización para la API REST;
- normalización de datos externos de TMDB;
- protección CSRF en operaciones de escritura;
- agrupación automática de sagas;
- separación entre estado y fase Kanban;
- validación backend del flujo Kanban;
- restricción de operaciones de modificación a `POST`;
- API REST pública de solo lectura.

El contexto, la decisión y el motivo de cada una se conservan en [Decisiones técnicas de CineTrack](../technical-decisions.md).
