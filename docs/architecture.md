# Arquitectura de CineTrack

## Enrutamiento

CineTrack utiliza un archivo `urls.py` propio para organizar las rutas de la aplicación.

Las rutas están agrupadas por funcionalidad:

- home, catálogo y detalle;
- CRUD de contenidos;
- búsqueda externa y guardado desde TMDB;
- agrupaciones de sagas;
- tablero Kanban de pendientes;
- favoritos;
- contenidos que el usuario volvería a ver;
- maratones;
- API REST.

## API REST

La API REST se expone bajo el prefijo `/api/`.

Actualmente, el recurso principal expuesto es `contenidos`, registrado mediante un `DefaultRouter` de Django REST Framework.

```text
/cinetrack/api/contenidos/
```

El router conecta el endpoint con `ContenidoViewSet`, permitiendo operaciones REST sobre la entidad `Contenido`.

## Separación entre vistas HTML y API REST

CineTrack mantiene dos interfaces sobre parte del mismo dominio:

- vistas HTML renderizadas con templates de Django;
- endpoints REST expuestos mediante Django REST Framework.

Esta separación permite que la aplicación funcione como producto web tradicional y, al mismo tiempo, exponga una API para consultar o manipular contenidos.

## Lógica de dominio

Parte de la lógica propia de CineTrack se encuentra separada en funciones auxiliares dentro de `utils.py`.

Un ejemplo relevante es la agrupación automática de sagas.

Esta lógica no pertenece directamente a las vistas porque no se encarga de recibir una petición HTTP ni de renderizar una respuesta. En cambio, representa una regla del dominio de la aplicación: determinar cuándo varios contenidos deben agruparse bajo una misma saga.

Separar esta lógica facilita su reutilización desde diferentes vistas y permite probarla de forma independiente.

## Construcción del dashboard principal

La vista `home` funciona como punto de composición del dashboard principal de CineTrack.

Su responsabilidad es obtener el conjunto base de contenidos, calcular los indicadores generales y construir el contexto necesario para renderizar `home.html`.

Los cálculos específicos del dashboard se encuentran separados en funciones auxiliares:

| Función | Responsabilidad |
| --- | --- |
| `calcular_promedio_calificacion` | Convierte las calificaciones categóricas a valores numéricos y calcula el promedio |
| `construir_barras_plataforma` | Agrupa contenidos por plataforma y calcula su representación porcentual |
| `obtener_top_calificados` | Obtiene los contenidos con mejor calificación |
| `obtener_tops_por_plataforma` | Obtiene los contenidos más vistos de cada plataforma |

Esta separación mantiene la vista enfocada en la composición de la respuesta y evita concentrar toda la lógica de cálculo del dashboard dentro de una única función.

### Representación numérica de calificaciones

CineTrack almacena las calificaciones como valores categóricos del dominio:

- Excelente
- Buena
- Regular
- Mala
- Horrible

Para realizar cálculos estadísticos y ordenar contenidos, estas categorías se transforman internamente a una escala numérica de `5` a `1`.

La conversión se centraliza mediante `CALIFICACION_NUMERICA`.

Esta representación numérica se utiliza únicamente para cálculos y ordenamiento. El modelo continúa almacenando la categoría original de la calificación.

### Reglas de agrupación y ordenamiento de sagas

La lógica relacionada con la identificación y organización de sagas se encuentra centralizada en `utils.py`.

Las vistas `catalogo` y `grupo_saga` reutilizan las mismas funciones auxiliares para determinar la clave de agrupación y ordenar los contenidos pertenecientes a una saga.

El orden interno considera:

1. la existencia de una posible continuación;
2. el año asociado al contenido;
3. el título en orden alfabético.

Centralizar esta regla evita mantener implementaciones duplicadas en diferentes vistas y garantiza que el catálogo y el detalle de una saga utilicen el mismo criterio de ordenamiento.

## Catálogo y agrupación de contenidos

La vista `catalogo` es responsable de mostrar el listado principal de contenidos registrados en CineTrack.

Para mantener la vista legible, la lógica se separa en funciones auxiliares:

| Función | Responsabilidad |
| --- | --- |
| `obtener_filtros_catalogo` | Lee y normaliza los filtros recibidos desde la URL |
| `aplicar_filtros_catalogo` | Aplica filtros al queryset de `Contenido` |
| `construir_grupos_catalogo` | Agrupa contenidos individuales y sagas para su presentación |
| `ordenar_contenidos_saga` | Define el orden interno de los contenidos dentro de una saga |

El catálogo permite combinar filtros por tipo, plataforma, estado, favoritos, contenidos que el usuario volvería a ver y búsqueda por título.

Después de aplicar los filtros, CineTrack agrupa los contenidos por saga cuando detecta más de un elemento relacionado. Los contenidos individuales se muestran como grupos de un solo elemento.

La paginación se aplica sobre los grupos resultantes, no directamente sobre cada contenido individual. Esto permite que una saga se mantenga unida visualmente dentro del catálogo.

### Contexto de agrupación en detalle y edición

Las vistas de detalle y edición necesitan identificar si un contenido pertenece a una agrupación de saga.

La función auxiliar `obtener_contexto_grupo_contenido` centraliza esta comprobación y construye el contexto compartido por ambas vistas.

El contexto incluye:

- `en_grupo`, que indica si existe más de un contenido asociado a la misma clave de saga;
- `clave_saga`, utilizada para navegar hacia la agrupación correspondiente cuando existe.

Centralizar esta lógica evita duplicar el cálculo de pertenencia a una saga entre las vistas de detalle y edición.

## Búsqueda externa y registro desde TMDB

CineTrack permite buscar películas y series en TMDB antes de registrarlas en el catálogo local.

La funcionalidad se divide entre la capa de vistas y la capa de integración.

```text
Formulario de búsqueda
        |
        v
buscar
        |
        v
buscar_contenido_tmdb
        |
        v
API de TMDB
        |
        v
Normalización de resultados
        |
        v
buscar.html
        |
        v
guardar_desde_busqueda
        |
        v
Contenido
```

La vista `buscar` recibe el término ingresado por el usuario y delega la consulta externa a `buscar_contenido_tmdb`.

La lógica HTTP y el manejo de errores de red permanecen encapsulados en `utils.py`. La vista trabaja únicamente con los resultados normalizados de la integración.

Cuando la búsqueda no produce resultados, la vista informa al usuario sin exponer detalles internos del servicio externo.

### Registro de resultados externos

La vista `guardar_desde_busqueda` transforma un resultado seleccionado de TMDB en una entidad `Contenido` persistida por CineTrack.

Antes de crear el registro, la vista valida:

- la existencia de un título;
- la selección de una plataforma;
- la ausencia de otro contenido con la misma combinación de título y plataforma.

La operación está restringida a peticiones `POST` y utiliza la protección CSRF de Django.

Cuando el estado no se recibe explícitamente, CineTrack utiliza `Contenido.Estado.PENDIENTE` como valor predeterminado.

## Gestión de maratones

CineTrack permite crear colecciones personalizadas de contenidos mediante la entidad `Maraton`.

Las vistas de maratones cubren las operaciones principales de gestión:

- listado de maratones;
- creación;
- consulta de detalle;
- edición;
- eliminación;
- eliminación de contenidos individuales de una colección.

La selección de contenidos se administra mediante `MaratonForm`, que trabaja sobre la relación `ManyToManyField` entre `Maraton` y `Contenido`.

Las operaciones destructivas, como eliminar un maratón o quitar un contenido de una colección, están restringidas a peticiones `POST`.

La lógica de las vistas se mantiene enfocada en recuperar entidades, validar formularios y coordinar las operaciones del modelo.

## Acceso de solo lectura

El recurso `Contenido` se expone mediante `ReadOnlyModelViewSet`.

La API permite:

- listar contenidos;
- consultar un contenido individual.

Las operaciones de creación, actualización y eliminación no se encuentran expuestas mediante la API REST.

```text
GET /api/contenidos/        -> Lista de contenidos
GET /api/contenidos/{id}/   -> Detalle de contenido
```

Las modificaciones de datos continúan realizándose mediante los flujos internos de la aplicación web.