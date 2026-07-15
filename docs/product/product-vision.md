# Visión de producto de CineTrack

## Propósito

CineTrack es una memoria audiovisual personal. Su propósito es ayudar a las personas a conservar y recuperar el contexto de las películas y series que consumen, no limitarse a mantener una lista de títulos.

## Problema que resuelve

Con el paso del tiempo, una persona puede olvidar episodios, personajes, relaciones, temporadas, conflictos abiertos, casos importantes o la razón por la que una historia le gustó o le impactó.

Las listas tradicionales permiten saber qué se vio, pero no necesariamente ayudan a reconstruir el estado de una historia ni a recuperar los recuerdos personales asociados con ella. CineTrack busca convertir el historial audiovisual en una fuente de contexto y memoria que resulte útil al retomar o recordar una obra.

## Estado actual

Actualmente, CineTrack permite:

- mantener un catálogo personal de películas y series;
- registrar contenido manualmente o a partir de resultados de TMDB;
- editar y eliminar contenido registrado;
- organizar contenidos por estado y fase de pendientes;
- registrar calificaciones y número de visualizaciones;
- marcar favoritos y contenidos que el usuario volvería a ver;
- agrupar contenidos relacionados en sagas;
- crear maratones;
- consultar contenidos mediante una API REST de solo lectura.

Estas capacidades constituyen la base actual del producto, pero no representan por sí solas su visión completa.

## Visión del producto

CineTrack debe evolucionar para ayudar al usuario a:

- recordar lo que vio;
- recuperar rápidamente el contexto antes de continuar una serie;
- conservar recuerdos personales relacionados con películas, temporadas o episodios;
- distinguir entre un resumen objetivo y una memoria o interpretación personal;
- recuperar el estado general de una historia, incluidos personajes, relaciones, eventos importantes y cabos sueltos;
- solicitar un recordatorio antes de continuar una historia;
- aprovechar su historial y sus recuerdos como base para una personalización futura.

La visión contempla la posible captura de notas breves o de voz y el uso de inteligencia artificial para apoyar la transcripción, organización o generación de resúmenes. Estas capacidades todavía no están implementadas y deben validarse antes de convertirse en compromisos de producto o decisiones técnicas.

## Principios del producto

### La memoria personal es central

El valor principal de CineTrack debe estar en ayudar al usuario a recordar y recuperar contexto, no solamente en registrar que consumió un contenido.

### La información objetiva y personal debe distinguirse

Una sinopsis externa, un resumen generado y un recuerdo escrito por el usuario tienen significados distintos. La experiencia debe conservar esa diferencia y evitar presentar interpretaciones personales como hechos objetivos.

### La procedencia debe ser clara

Cuando una información provenga del usuario, de TMDB, de otra fuente externa o de un proceso asistido por inteligencia artificial, su origen debe poder reconocerse.

### El usuario debe conservar el control

Los recuerdos, notas y posibles grabaciones pertenecen a la experiencia personal del usuario. Su uso futuro debe considerar control, privacidad y capacidad de revisión.

### La evolución debe ser gradual

La visión orienta el producto, pero no obliga a diseñar o implementar anticipadamente todos sus conceptos. Cada capacidad debe validarse antes de incorporarse al sistema.

## Alcance de este documento

Este documento define el problema, la identidad y los principios de CineTrack. No establece fechas, modelos de datos, proveedores, decisiones de arquitectura ni compromisos de implementación. La secuencia de evolución se mantiene en el [roadmap del producto](roadmap.md).

