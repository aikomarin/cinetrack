# Decisiones técnicas de CineTrack

Este documento registra las decisiones de diseño y mantenimiento más relevantes tomadas durante el desarrollo y evolución de CineTrack.

## Uso de TextChoices para valores controlados

Los valores de tipo, estado, plataforma, calificación y fase Kanban se definen mediante `models.TextChoices`.

### Contexto

La implementación inicial utilizaba listas de tuplas como `choices` de Django.

Aunque esta implementación era funcional, diferentes partes de la aplicación necesitaban utilizar directamente valores literales como `pendiente`, `vista`, `nuevo` o `encurso`.

### Decisión

Centralizar los valores controlados del dominio mediante clases `TextChoices` dentro del modelo `Contenido`.

### Motivo

Esta estructura permite:

- centralizar los valores válidos del dominio;
- reducir el uso de strings literales en la lógica de la aplicación;
- mejorar la legibilidad del código;
- facilitar futuros cambios en las opciones disponibles.

---

## Restricción de visualizaciones a valores positivos

El campo `veces_vista` fue modificado de `IntegerField` a `PositiveIntegerField`.

### Contexto

El número de visualizaciones representa una cantidad y, por definición del dominio, no puede tener valores negativos.

La implementación inicial permitía técnicamente almacenar valores menores a cero.

### Decisión

Utilizar `PositiveIntegerField` para representar directamente la restricción natural del dominio.

### Motivo

El modelo de datos debe reflejar las reglas del dominio siempre que sea posible, reduciendo la posibilidad de almacenar estados inválidos.

---

## Migración de Star+ a Disney+

La plataforma Star+ dejó de mantenerse como una opción independiente dentro de CineTrack.

### Contexto

Existían registros históricos almacenados con el valor interno `star`.

Eliminar directamente Star+ de las opciones disponibles habría dejado registros existentes con un valor que ya no pertenecía al conjunto válido de plataformas definido por la aplicación.

### Decisión

Realizar una migración de datos para actualizar los registros existentes de `star` a `disney` antes de eliminar Star+ de las opciones del modelo.

La transformación se implementó mediante una migración de datos con `RunPython`.

### Motivo

La migración permite mantener la consistencia entre los datos históricos y las opciones válidas del dominio sin eliminar contenidos existentes ni requerir modificaciones manuales en la base de datos.

---

## Separación entre estado y fase Kanban

CineTrack mantiene los campos `estado` y `fase_kanban` como conceptos independientes dentro del modelo `Contenido`.

### Contexto

Ambos campos representan información relacionada con el seguimiento de contenido, pero responden a preguntas diferentes.

`estado` indica si un contenido ya fue visto o continúa pendiente.

`fase_kanban` representa la etapa de intención de visualización de un contenido pendiente.

### Decisión

Mantener ambos conceptos como campos independientes.

### Motivo

Separar ambas dimensiones permite administrar el historial de visualización sin acoplarlo al flujo Kanban.

Un contenido puede conservar su información de seguimiento general mientras el tablero representa exclusivamente la organización de contenidos pendientes.

---

## Contrato explícito de serialización para la API REST

La API REST de CineTrack utiliza un `ModelSerializer` para representar la entidad `Contenido`.

### Contexto

La implementación inicial utilizaba `fields = "__all__"`.

Esta configuración expone automáticamente todos los campos definidos en el modelo y puede provocar que nuevos campos sean incorporados a la API sin una decisión explícita sobre su exposición.

### Decisión

Definir de forma explícita los campos incluidos en `ContenidoSerializer`.

Los campos `id`, `created_at` y `updated_at` se mantienen como campos de solo lectura.

### Motivo

Mantener una lista explícita de campos permite tratar el serializer como parte del contrato público de la API.

De esta forma, los cambios futuros en el modelo no modifican automáticamente la representación REST de `Contenido` y los campos administrados por el sistema no pueden ser modificados directamente por los clientes de la API.


## Normalización de datos externos de TMDB

### Contexto

TMDB utiliza estructuras parcialmente diferentes para representar películas y series.

Los títulos y fechas, por ejemplo, se reciben mediante campos distintos según el tipo de contenido consultado.

### Decisión

Encapsular la integración con TMDB en una capa de utilidades y transformar las respuestas externas a una estructura común antes de utilizarlas en las vistas de CineTrack.

### Motivo

La normalización evita propagar detalles específicos de la API externa al resto de la aplicación.

Las vistas y formularios pueden trabajar con una representación estable de contenido independientemente de si el resultado original corresponde a una película o una serie.

---

## Protección CSRF en operaciones de escritura

### Contexto

La vista `guardar_desde_busqueda` permite crear nuevos registros de `Contenido` a partir de resultados obtenidos desde TMDB.

La implementación inicial utilizaba el decorador `@csrf_exempt`, deshabilitando la validación CSRF de Django para esta operación.

El formulario utilizado por CineTrack ya enviaba correctamente el token CSRF, por lo que la exención no era necesaria.

### Decisión

Eliminar `@csrf_exempt` y mantener activa la protección CSRF proporcionada por Django.

La vista también fue restringida explícitamente a peticiones `POST` mediante el decorador `@require_POST`.

### Motivo

Las operaciones que modifican datos deben validar que la petición provenga de un flujo legítimo de la aplicación.

Mantener la protección CSRF reduce el riesgo de solicitudes de escritura originadas desde sitios externos, mientras que la restricción a `POST` expresa de forma explícita que la vista realiza una operación de modificación sobre el sistema.

---

## Agrupación automática de sagas

### Contexto

CineTrack agrupa contenidos relacionados en sagas a partir del título de cada película o serie.

La implementación no utiliza un modelo `Saga` ni una relación directa desde `Contenido`.

### Decisión

Calcular dinámicamente una clave de saga mediante la función `clave_saga_desde_titulo`.

La función normaliza el título del contenido mediante reglas como:

- conversión a minúsculas;
- eliminación de acentos;
- eliminación de artículos iniciales;
- separación de subtítulos;
- limpieza de números y numerales romanos;
- detección de franquicias conocidas.

Cuando el nombre generado automáticamente no es suficientemente claro, `SagaAlias` permite guardar un nombre visible personalizado.

### Motivo

Esta estrategia evita agregar una entidad adicional al modelo de datos cuando la pertenencia a una saga puede inferirse razonablemente desde el título.

También permite combinar automatización con corrección manual mediante alias, manteniendo el modelo principal más simple.

---

## Validación backend del flujo Kanban

### Contexto

El tablero Kanban de CineTrack muestra únicamente contenidos con estado pendiente.

Aunque la interfaz no permite mover contenidos ya vistos entre fases Kanban, una petición HTTP podría construirse manualmente contra el endpoint encargado de mover fases.

### Decisión

La vista `mover_fase` valida que el contenido exista y que su estado sea `Contenido.Estado.PENDIENTE` antes de permitir el cambio de fase.

### Motivo

Las reglas del dominio no deben depender únicamente del frontend.

Validar la condición en el backend garantiza que solamente los contenidos pendientes puedan moverse dentro del flujo Kanban.

---

## Restricción de operaciones de modificación a POST

### Contexto

Algunas vistas de CineTrack realizan modificaciones sobre datos existentes, como eliminar contenidos, guardar resultados externos o renombrar sagas.

### Decisión

Las vistas que modifican información se restringen explícitamente a peticiones `POST` mediante `@require_POST`.

### Motivo

Esto separa las operaciones de lectura y escritura, evita modificaciones accidentales mediante peticiones `GET` y hace más clara la intención de cada endpoint.

---

## API REST pública de solo lectura

### Contexto

CineTrack expone información de la entidad `Contenido` mediante una API REST construida con Django REST Framework.

La implementación inicial utilizaba `ModelViewSet`, habilitando automáticamente operaciones de lectura y escritura sobre el recurso.

Esto permitía listar y consultar contenidos, pero también crear, modificar y eliminar registros mediante la API.

Actualmente, CineTrack no implementa un sistema de autenticación específico para proteger las operaciones de escritura de la API.

### Decisión

Utilizar `ReadOnlyModelViewSet` para exponer el recurso `Contenido`.

La API permite únicamente las operaciones de listado y consulta individual mediante peticiones `GET`.

Las operaciones `POST`, `PUT`, `PATCH` y `DELETE` no están disponibles.

### Motivo

La API forma parte del portafolio técnico de CineTrack y permite demostrar la exposición de recursos mediante Django REST Framework.

Mantenerla como solo lectura permite consultar los datos del sistema sin exponer operaciones que puedan modificar la base de datos públicamente.

Las operaciones de escritura podrán habilitarse en el futuro cuando exista un mecanismo de autenticación y permisos adecuado.