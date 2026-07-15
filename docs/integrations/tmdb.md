# Integraciones de CineTrack

## TMDB

CineTrack utiliza la API de TMDB como fuente externa para la búsqueda de películas y series.

La integración se encuentra encapsulada en `cinetrack/utils.py`, separando el consumo del servicio externo de la lógica de las vistas de Django.

### Flujo de búsqueda

La búsqueda consulta dos tipos de contenido de TMDB:

- películas mediante el recurso `movie`;
- series mediante el recurso `tv`.

Los resultados de ambas consultas se transforman a una representación común utilizada internamente por CineTrack.

```text
Consulta del usuario
        |
        v
buscar_contenido_tmdb
        |
        +---- movie
        |
        +---- tv
        |
        v
Normalización de resultados
        |
        v
Formato interno de CineTrack
```


### Normalización de datos

Las respuestas de TMDB utilizan campos diferentes para películas y series.

Por ejemplo, el título puede encontrarse en `title` o `name`, mientras que la fecha puede recibirse como `release_date` o `first_air_date`.

CineTrack transforma estas diferencias a una estructura común:

| Campo interno | Origen en TMDB |
| --- | --- |
| `titulo` | `title` o `name` |
| `resumen` | `overview` |
| `fecha` | `release_date` o `first_air_date` |
| `imagen` | `poster_path` |
| `tipo` | Tipo de recurso consultado |

Esta normalización evita que el resto de la aplicación dependa directamente de las diferencias entre las respuestas de películas y series.

### Manejo de fechas

Las fechas recibidas desde TMDB se convierten al tipo `date` utilizado por el modelo de CineTrack.

Si el servicio externo no proporciona una fecha o devuelve un valor que no cumple con el formato esperado `YYYY-MM-DD`, la aplicación utiliza `None`.

Esta transformación evita propagar valores de fecha inválidos al resto de la aplicación.

### Construcción de imágenes

TMDB proporciona la ruta relativa del póster mediante `poster_path`.

CineTrack combina esta ruta con la URL base de imágenes de TMDB para generar una URL completa utilizando el tamaño `w500`.

Cuando un resultado no contiene un póster, el campo de imagen se representa mediante una cadena vacía.

### Manejo de errores externos

Las solicitudes a TMDB utilizan un tiempo máximo de espera de 10 segundos para evitar que una respuesta lenta bloquee indefinidamente la búsqueda.

Los errores HTTP, problemas de conexión y otras excepciones asociadas a la solicitud se capturan mediante `requests.RequestException`.

Cuando una consulta externa falla, la integración devuelve una colección vacía para ese tipo de contenido y permite que la aplicación mantenga el control del flujo.

### Configuración

La clave utilizada para consumir la API de TMDB se obtiene desde la configuración de Django mediante `settings.TMDB_API_KEY`.

La integración no define credenciales directamente dentro de `utils.py`.

La gestión de secretos y variables de entorno se documentará como parte de la configuración de producción de CineTrack.