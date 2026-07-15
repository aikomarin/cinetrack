# ADR-0006: Proteger escrituras web mediante POST y CSRF

## Estado

Vigente.

## Contexto

La interfaz web contiene formularios y acciones que modifican información. La vista `guardar_desde_busqueda` utilizó inicialmente `csrf_exempt` aunque su formulario ya enviaba el token CSRF.

Las mutaciones no deben ejecutarse mediante solicitudes GET ni depender únicamente de controles del frontend.

## Decisión

Mantener habilitada la protección CSRF de Django para las escrituras de la interfaz web y realizar las mutaciones mediante solicitudes POST.

Los endpoints dedicados exclusivamente a acciones de escritura se restringen mediante `require_POST`. Las vistas que también muestran formularios pueden aceptar GET, pero solo aplican cambios en su rama POST.

## Consecuencias

- Las consultas GET no deben provocar mutaciones.
- Los formularios deben incluir un token CSRF válido.
- Las solicitudes JavaScript que modifican datos deben enviar el token CSRF.
- Las reglas de método y protección se aplican en backend y no dependen exclusivamente de la interfaz.

## Alternativas consideradas

- Mantener `csrf_exempt` en operaciones de escritura.
- Permitir que una solicitud GET modifique datos.

Ambas alternativas reducen las protecciones proporcionadas por el flujo estándar de Django.

