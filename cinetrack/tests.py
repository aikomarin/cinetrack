import re
from datetime import date
from html import unescape
from unittest.mock import patch
from urllib.parse import quote

from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils.html import escape

from .catalog.pagination import obtener_rango_paginas
from .content.images import resolver_url_portada
from .models import Contenido, Maraton


@override_settings(
    STORAGES={
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
)
class ContenidoFormViewsTests(TestCase):
    def setUp(self):
        self.contenido = Contenido.objects.create(
            titulo="Alien",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.DISNEY,
        )
        self.datos_validos = {
            "titulo": "Blade Runner",
            "resumen": "",
            "fecha": "",
            "tipo": Contenido.Tipo.PELICULA,
            "plataforma": Contenido.Plataforma.PRIME,
            "calificacion": "",
            "veces_vista": 0,
            "estado": Contenido.Estado.PENDIENTE,
            "volveria_a_ver": "",
            "tendra_continuacion": "",
            "favorita": "",
        }

    def test_registrar_guarda_y_redirige_al_catalogo(self):
        response = self.client.post(reverse("cinetrack:registrar"), self.datos_validos)

        self.assertRedirects(response, reverse("cinetrack:catalogo"))
        self.assertTrue(
            Contenido.objects.filter(
                titulo="Blade Runner",
                plataforma=Contenido.Plataforma.PRIME,
            ).exists()
        )

    def test_registrar_muestra_error_para_titulo_y_plataforma_duplicados(self):
        datos = {
            **self.datos_validos,
            "titulo": self.contenido.titulo,
            "plataforma": self.contenido.plataforma,
        }

        response = self.client.post(reverse("cinetrack:registrar"), datos)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Este contenido ya fue registrado previamente.")
        self.assertEqual(Contenido.objects.count(), 1)

    def test_editar_permite_conservar_titulo_y_plataforma(self):
        datos = {
            **self.datos_validos,
            "titulo": self.contenido.titulo,
            "plataforma": self.contenido.plataforma,
            "resumen": "Actualizado",
        }

        response = self.client.post(
            reverse("cinetrack:editar", args=[self.contenido.pk]),
            datos,
        )

        self.assertRedirects(
            response,
            reverse("cinetrack:detalle", args=[self.contenido.pk]),
        )
        self.contenido.refresh_from_db()
        self.assertEqual(self.contenido.resumen, "Actualizado")

    def test_editar_rechaza_duplicado_de_otro_contenido(self):
        otro = Contenido.objects.create(
            titulo="Blade Runner",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.PRIME,
        )
        datos = {
            **self.datos_validos,
            "titulo": self.contenido.titulo,
            "plataforma": self.contenido.plataforma,
        }

        response = self.client.post(
            reverse("cinetrack:editar", args=[otro.pk]),
            datos,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Este contenido ya fue registrado previamente.")
        otro.refresh_from_db()
        self.assertEqual(otro.titulo, "Blade Runner")

    def test_editar_desde_catalogo_conserva_toda_la_query(self):
        retorno = (
            reverse("cinetrack:catalogo")
            + "?q=alien&plataforma=disney&tipo=pelicula"
            + "&estado=pendiente&favorita=1&page=3&futuro=valor"
        )
        response = self.client.post(
            reverse("cinetrack:editar", args=[self.contenido.pk])
            + "?origen=catalogo&page=3&return_to="
            + quote(retorno, safe=""),
            {
                **self.datos_validos,
                "titulo": self.contenido.titulo,
                "plataforma": self.contenido.plataforma,
            },
        )

        self.assertRedirects(
            response,
            retorno,
        )

    def test_editar_rechaza_retorno_externo_y_usa_fallback(self):
        response = self.client.post(
            reverse("cinetrack:editar", args=[self.contenido.pk])
            + "?origen=catalogo&page=3&return_to="
            + quote("https://example.com/robo", safe=""),
            {
                **self.datos_validos,
                "titulo": self.contenido.titulo,
                "plataforma": self.contenido.plataforma,
            },
        )

        self.assertRedirects(
            response,
            reverse("cinetrack:catalogo") + "?page=3",
        )

    def test_editar_desde_grupo_regresa_al_grupo(self):
        Contenido.objects.create(
            titulo="Alien 2",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.PRIME,
        )
        response = self.client.post(
            reverse("cinetrack:editar", args=[self.contenido.pk])
            + "?origen=grupo&page=2",
            {
                **self.datos_validos,
                "titulo": self.contenido.titulo,
                "plataforma": self.contenido.plataforma,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn("/grupo/alien/", response.url)
        self.assertTrue(response.url.endswith("?page=2"))

    def test_error_obligatorio_conserva_los_datos_ingresados(self):
        response = self.client.post(
            reverse("cinetrack:registrar"),
            {
                **self.datos_validos,
                "titulo": "Dato conservado",
                "tipo": "",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("tipo", response.context["formulario"].errors)
        self.assertContains(response, "Este campo es requerido.")
        self.assertContains(response, 'value="Dato conservado"')
        self.assertFalse(
            Contenido.objects.filter(titulo="Dato conservado").exists()
        )

    def test_selects_muestran_etiquetas_vacias_legibles(self):
        response = self.client.get(reverse("cinetrack:registrar"))

        self.assertNotContains(response, "---------")
        self.assertContains(response, "Selecciona un tipo")
        self.assertContains(response, "Sin plataforma")
        self.assertContains(response, "Sin calificación")

    def assert_editar_muestra_retorno_en_volver_y_cancelar(
        self,
        url_editar,
        url_retorno,
    ):
        response = self.client.get(url_editar)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["url_retorno"], url_retorno)
        self.assertEqual(
            response.content.decode().count(
                f'href="{escape(url_retorno)}"'
            ),
            2,
        )
        self.assertContains(response, "Cancelar")

    def test_editar_cancelar_regresa_al_detalle(self):
        self.assert_editar_muestra_retorno_en_volver_y_cancelar(
            reverse("cinetrack:editar", args=[self.contenido.pk])
            + "?origen=detalle",
            reverse("cinetrack:detalle", args=[self.contenido.pk]),
        )

    def test_editar_cancelar_conserva_filtros_del_catalogo(self):
        retorno = reverse("cinetrack:catalogo") + "?q=alien&page=3&futuro=valor"
        self.assert_editar_muestra_retorno_en_volver_y_cancelar(
            reverse("cinetrack:editar", args=[self.contenido.pk])
            + "?origen=catalogo&page=3&return_to="
            + quote(retorno, safe=""),
            retorno,
        )

    def test_editar_cancelar_regresa_al_grupo(self):
        Contenido.objects.create(
            titulo="Alien 2",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.PRIME,
        )
        retorno = reverse("cinetrack:grupo_saga", args=["alien"]) + "?page=2"
        self.assert_editar_muestra_retorno_en_volver_y_cancelar(
            reverse("cinetrack:editar", args=[self.contenido.pk])
            + "?origen=grupo&page=2",
            retorno,
        )

    def test_registrar_conserva_cancelar_al_catalogo(self):
        response = self.client.get(reverse("cinetrack:registrar"))

        self.assertContains(response, "Cancelar")
        self.assertContains(
            response,
            f'href="{reverse("cinetrack:catalogo")}" class="btn-ghost"',
        )


@override_settings(
    STORAGES={
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
)
class DetalleContenidoTests(TestCase):
    def setUp(self):
        self.contenido = Contenido.objects.create(
            titulo="Arrival",
            resumen="Primer contacto.",
            imagen="https://example.com/arrival.jpg",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.PRIME,
            estado=Contenido.Estado.PENDIENTE,
            favorita=True,
        )
        self.url = reverse(
            "cinetrack:detalle",
            args=[self.contenido.pk],
        )

    def test_detalle_carga_informacion_y_fondo_sin_estilo_inline(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.contenido.titulo)
        self.assertContains(response, self.contenido.imagen, count=2)
        self.assertNotContains(response, 'class="detail-bg" style=')
        self.assertContains(response, "Primer contacto.")

    def test_favorita_pendiente_muestra_un_valor_coherente(self):
        response = self.client.get(self.url)

        self.assertContains(
            response,
            '<dt class="label">Favorita</dt><dd class="value">Sí</dd>',
            html=True,
        )

    def test_retorno_al_catalogo_conserva_toda_la_query(self):
        retorno = (
            reverse("cinetrack:catalogo")
            + "?q=arrival&estado=pendiente&page=2&futuro=valor"
        )
        response = self.client.get(
            self.url
            + "?origen=catalogo&page=2&return_to="
            + quote(retorno, safe="")
        )

        self.assertEqual(response.context["url_retorno"], retorno)
        self.assertContains(response, "Volver al catálogo")

    def test_retorno_externo_usa_fallback_del_catalogo(self):
        response = self.client.get(
            self.url
            + "?origen=catalogo&page=2&return_to="
            + quote("https://example.com/robo", safe="")
        )

        self.assertEqual(
            response.context["url_retorno"],
            reverse("cinetrack:catalogo") + "?page=2",
        )

    def test_destinos_de_retorno_de_origenes_fijos(self):
        destinos = {
            "favoritos": reverse("cinetrack:favoritos"),
            "pendientes": reverse("cinetrack:pendientes"),
            "volveria_a_ver": reverse("cinetrack:volverias"),
        }

        for origen, destino in destinos.items():
            with self.subTest(origen=origen):
                response = self.client.get(
                    self.url + f"?origen={origen}"
                )
                self.assertEqual(response.context["url_retorno"], destino)

    def test_retorno_a_maraton(self):
        maraton = Maraton.objects.create(nombre="Ciencia ficción")
        maraton.contenidos.add(self.contenido)

        response = self.client.get(
            self.url + f"?origen=maraton&maraton_id={maraton.pk}"
        )

        self.assertEqual(
            response.context["url_retorno"],
            reverse("cinetrack:detalle_maraton", args=[maraton.pk]),
        )

    def test_retorno_a_grupo_conserva_pagina(self):
        Contenido.objects.create(
            titulo="Arrival 2",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.DISNEY,
        )

        response = self.client.get(
            self.url + "?origen=grupo&page=3"
        )

        self.assertEqual(
            response.context["url_retorno"],
            reverse("cinetrack:grupo_saga", args=["arrival"])
            + "?page=3",
        )


@override_settings(
    STORAGES={
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
)
class CatalogoBusquedaTests(TestCase):
    def setUp(self):
        self.alien = Contenido.objects.create(
            titulo="Alien",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.DISNEY,
            estado=Contenido.Estado.PENDIENTE,
            favorita=True,
        )
        self.arrival = Contenido.objects.create(
            titulo="Arrival",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.PRIME,
            estado=Contenido.Estado.VISTA,
            favorita=True,
            volveria_a_ver=True,
        )
        self.casablanca = Contenido.objects.create(
            titulo="Casablanca",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.HBO,
            estado=Contenido.Estado.VISTA,
            favorita=True,
        )
        self.dark = Contenido.objects.create(
            titulo="Dark",
            tipo=Contenido.Tipo.SERIE,
            plataforma=Contenido.Plataforma.NETFLIX,
            estado=Contenido.Estado.VISTA,
        )

    def test_catalogo_combina_filtros(self):
        response = self.client.get(
            reverse("cinetrack:catalogo"),
            {
                "tipo": "pelicula",
                "plataforma": "prime",
                "estado": "vista",
                "favorita": "1",
                "volveria_a_ver": "1",
                "buscar": "rri",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["total_contenidos"], 1)
        self.assertContains(response, "Arrival")
        self.assertNotContains(response, "Alien")

    def test_rango_paginacion_al_inicio(self):
        self.assertEqual(
            list(obtener_rango_paginas(1, 10)),
            [1, 2, 3, 4, 5],
        )

    def test_rango_paginacion_intermedio(self):
        self.assertEqual(
            list(obtener_rango_paginas(4, 10)),
            [2, 3, 4, 5, 6],
        )

    def test_rango_paginacion_al_final(self):
        self.assertEqual(
            list(obtener_rango_paginas(9, 10)),
            [6, 7, 8, 9, 10],
        )
        self.assertEqual(
            list(obtener_rango_paginas(10, 10)),
            [6, 7, 8, 9, 10],
        )

    def test_rango_paginacion_de_una_sola_pagina(self):
        self.assertEqual(list(obtener_rango_paginas(1, 1)), [1])

    def test_una_sola_pagina_no_muestra_enlaces_inexistentes(self):
        response = self.client.get(
            reverse("cinetrack:catalogo"),
            {"tipo": "serie", "buscar": "Dark"},
        )

        self.assertEqual(
            response.context["paginacion"]["paginas"],
            [{
                "numero": 1,
                "actual": True,
                "url": "?tipo=serie&buscar=Dark&page=1",
            }],
        )
        self.assertContains(response, 'aria-current="page"')
        self.assertNotContains(response, ">Siguiente</a>")
        self.assertNotContains(response, ">Anterior</a>")
        self.assertNotContains(response, "page=2")

    @patch("cinetrack.catalog.views.CATALOGO_POR_PAGINA", 2)
    def test_enlaces_numericos_sustituyen_solo_page(self):
        for titulo in ("Matrix", "Gravity", "Avatar"):
            Contenido.objects.create(
                titulo=titulo,
                tipo=Contenido.Tipo.PELICULA,
                plataforma=Contenido.Plataforma.HBO,
                estado=Contenido.Estado.VISTA,
            )

        response = self.client.get(
            reverse("cinetrack:catalogo")
            + "?page=2&tipo=pelicula&estado=vista"
            + "&buscar=a&futuro=valor",
        )

        self.assertContains(
            response,
            'href="?page=1&amp;tipo=pelicula&amp;estado=vista'
            '&amp;buscar=a&amp;futuro=valor"',
        )
        self.assertContains(
            response,
            'href="?page=3&amp;tipo=pelicula&amp;estado=vista'
            '&amp;buscar=a&amp;futuro=valor"',
        )
        self.assertContains(
            response,
            '<li class="page-item active" aria-current="page">'
            '\n            <span class="page-link">2</span>',
            html=True,
        )
        self.assertNotContains(
            response,
            'href="?page=2&amp;tipo=pelicula&amp;estado=vista'
            '&amp;buscar=a&amp;futuro=valor">2</a>',
        )

    @patch("cinetrack.catalog.views.CATALOGO_POR_PAGINA", 2)
    def test_paginacion_conserva_query_completa_y_parametros_futuros(self):
        response = self.client.get(
            reverse("cinetrack:catalogo")
            + "?tipo=pelicula&favorita=1&futuro=valor&page=1"
        )

        self.assertContains(
            response,
            "?tipo=pelicula&amp;favorita=1&amp;futuro=valor&amp;page=2",
        )

    def test_tarjetas_de_detalle_y_editar_conservan_catalogo_completo(self):
        query = "tipo=pelicula&plataforma=disney&favorita=1&page=1"
        response = self.client.get(
            reverse("cinetrack:catalogo") + "?" + query
        )
        retorno = quote(
            reverse("cinetrack:catalogo") + "?" + query,
            safe="/",
        )

        self.assertContains(response, f"return_to={retorno}", count=3)

    def test_catalogo_muestra_estado_vacio(self):
        response = self.client.get(
            reverse("cinetrack:catalogo"),
            {"buscar": "No existe en la colección"},
        )

        self.assertContains(response, "Sin resultados")
        self.assertEqual(response.context["total_contenidos"], 0)

    @patch("cinetrack.catalog.views.CATALOGO_POR_PAGINA", 2)
    def test_formulario_renderizado_envia_retorno_completo(self):
        for titulo in (
            "Alpha One",
            "Bravo Two",
            "Charlie Three",
            "Delta Four",
            "Echo Five",
        ):
            Contenido.objects.create(
                titulo=titulo,
                tipo=Contenido.Tipo.PELICULA,
                plataforma=Contenido.Plataforma.HBO,
                estado=Contenido.Estado.VISTA,
            )

        query = "page=3&tipo=pelicula&estado=vista"
        retorno = reverse("cinetrack:catalogo") + "?" + query
        response = self.client.get(
            retorno
        )
        html = response.content.decode()
        formulario = re.search(
            r'<form id="del-(?P<pk>\d+)" method="post" '
            r'action="(?P<action>[^"]+)" class="d-none">'
            r'(?P<body>.*?)</form>',
            html,
            re.DOTALL,
        )

        self.assertIsNotNone(formulario)
        action = unescape(formulario.group("action"))
        hidden = re.search(
            r'<input type="hidden" name="return_to" value="([^"]+)">',
            formulario.group("body"),
        )
        self.assertIsNotNone(hidden)
        retorno_hidden = unescape(hidden.group(1))
        action_esperado = (
            reverse(
                "cinetrack:eliminar",
                args=[int(formulario.group("pk"))],
            )
            + "?return_to="
            + quote(retorno, safe="/")
        )

        self.assertEqual(action, action_esperado)
        self.assertEqual(retorno_hidden, retorno)

        post_response = self.client.post(
            action,
            {"return_to": retorno_hidden},
        )
        self.assertRedirects(post_response, retorno)

    @patch("cinetrack.catalog.views.CATALOGO_POR_PAGINA", 2)
    def test_eliminar_conserva_busqueda_filtros_parametros_y_pagina(self):
        matrix = Contenido.objects.create(
            titulo="Matrix",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.HBO,
            estado=Contenido.Estado.VISTA,
        )
        Contenido.objects.create(
            titulo="Gravity",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.HBO,
            estado=Contenido.Estado.VISTA,
        )
        Contenido.objects.create(
            titulo="Avatar",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.HBO,
            estado=Contenido.Estado.VISTA,
        )
        retorno = (
            reverse("cinetrack:catalogo")
            + "?tipo=pelicula&plataforma=hbo&estado=vista"
            + "&buscar=a&futuro=valor&page=2"
        )
        response = self.client.post(
            reverse("cinetrack:eliminar", args=[matrix.pk])
            + "?return_to="
            + quote(retorno, safe=""),
            {"return_to": retorno},
            follow=True,
        )

        self.assertEqual(response.redirect_chain, [(retorno, 302)])
        self.assertEqual(response.request["QUERY_STRING"], retorno.split("?", 1)[1])
        self.assertEqual(response.context["page_obj"].number, 2)
        self.assertFalse(Contenido.objects.filter(pk=matrix.pk).exists())

    @patch("cinetrack.catalog.views.CATALOGO_POR_PAGINA", 2)
    def test_eliminar_ultima_tarjeta_regresa_a_ultima_pagina_valida(self):
        for titulo in ("Kappa", "Lambda", "Omega"):
            contenido = Contenido.objects.create(
                titulo=titulo,
                tipo=Contenido.Tipo.PELICULA,
                plataforma=Contenido.Plataforma.OTRO,
                estado=Contenido.Estado.PENDIENTE,
            )

        retorno = (
            reverse("cinetrack:catalogo")
            + "?plataforma=otro&futuro=valor&page=2"
        )
        pagina_valida = (
            reverse("cinetrack:catalogo")
            + "?plataforma=otro&futuro=valor&page=1"
        )
        response = self.client.post(
            reverse("cinetrack:eliminar", args=[contenido.pk]),
            {"return_to": retorno},
            follow=True,
        )

        self.assertEqual(
            response.redirect_chain,
            [(pagina_valida, 302)],
        )
        self.assertEqual(response.context["page_obj"].number, 1)
        self.assertEqual(
            response.request["QUERY_STRING"],
            "plataforma=otro&futuro=valor&page=1",
        )

    def test_eliminar_rechaza_retorno_externo(self):
        response = self.client.post(
            reverse("cinetrack:eliminar", args=[self.alien.pk])
            + "?return_to=https%3A%2F%2Fexample.com%2Fexterno",
        )

        self.assertRedirects(response, reverse("cinetrack:catalogo"))

    def test_eliminar_usa_retorno_post_si_la_query_es_invalida(self):
        retorno = reverse("cinetrack:catalogo") + "?favorita=1&page=1"
        response = self.client.post(
            reverse("cinetrack:eliminar", args=[self.alien.pk])
            + "?return_to=https%3A%2F%2Fexample.com%2Fexterno",
            {"return_to": retorno},
        )

        self.assertRedirects(response, retorno)

    @patch("cinetrack.catalog.views.buscar_contenido_tmdb")
    def test_busqueda_get_muestra_resultados(self, buscar_mock):
        buscar_mock.return_value = [{
            "titulo": "Dune",
            "resumen": "Arrakis.",
            "fecha": date(2021, 10, 22),
            "imagen": "https://example.com/dune.jpg",
            "tipo": Contenido.Tipo.PELICULA,
        }]

        response = self.client.get(
            reverse("cinetrack:buscar"),
            {"query": "Dune"},
        )

        buscar_mock.assert_called_once_with("Dune")
        self.assertContains(response, "Resultados")
        self.assertContains(response, "Arrakis.")
        self.assertContains(response, 'name="query" value="Dune"')

    @patch("cinetrack.catalog.views.buscar_contenido_tmdb", return_value=[])
    def test_busqueda_sin_coincidencias_muestra_estado_vacio(self, buscar_mock):
        response = self.client.get(
            reverse("cinetrack:buscar"),
            {"query": "Inexistente"},
        )

        self.assertContains(response, "Sin resultados")
        self.assertNotContains(
            response,
            "TMDB no respondió correctamente",
        )

    @patch("cinetrack.catalog.views.buscar_contenido_tmdb")
    def test_busqueda_vacia_no_consulta_proveedor(self, buscar_mock):
        response = self.client.get(
            reverse("cinetrack:buscar"),
            {"query": ""},
        )

        buscar_mock.assert_not_called()
        self.assertContains(response, "Este campo es requerido.")

    def test_guardar_desde_busqueda_valida_y_restaura_busqueda(self):
        response = self.client.post(
            reverse("cinetrack:guardar_desde_busqueda"),
            {
                "query": "Dune",
                "titulo": "Dune",
                "resumen": "Arrakis.",
                "fecha": "2021-10-22",
                "imagen": "https://example.com/dune.jpg",
                "tipo": Contenido.Tipo.PELICULA,
                "plataforma": Contenido.Plataforma.HBO,
                "estado": Contenido.Estado.PENDIENTE,
                "calificacion": "",
                "veces_vista": "0",
            },
        )

        self.assertRedirects(
            response,
            reverse("cinetrack:buscar") + "?query=Dune",
        )
        self.assertTrue(
            Contenido.objects.filter(
                titulo="Dune",
                plataforma=Contenido.Plataforma.HBO,
                imagen="https://example.com/dune.jpg",
            ).exists()
        )

    def test_guardar_desde_busqueda_normaliza_path_relativo_tmdb(self):
        response = self.client.post(
            reverse("cinetrack:guardar_desde_busqueda"),
            {
                "query": "Dune",
                "titulo": "Dune",
                "resumen": "Arrakis.",
                "fecha": "2021-10-22",
                "imagen": "/poster/dune.jpg",
                "tipo": Contenido.Tipo.PELICULA,
                "plataforma": Contenido.Plataforma.HBO,
                "estado": Contenido.Estado.PENDIENTE,
                "calificacion": "",
                "veces_vista": "0",
            },
        )

        self.assertRedirects(
            response,
            reverse("cinetrack:buscar") + "?query=Dune",
        )
        self.assertEqual(
            Contenido.objects.get(titulo="Dune").imagen,
            "https://image.tmdb.org/t/p/w500/poster/dune.jpg",
        )

    def test_guardar_desde_busqueda_rechaza_datos_invalidos(self):
        response = self.client.post(
            reverse("cinetrack:guardar_desde_busqueda"),
            {
                "query": "Dune",
                "titulo": "Dune",
                "tipo": "documental",
                "plataforma": Contenido.Plataforma.HBO,
                "estado": Contenido.Estado.PENDIENTE,
                "veces_vista": "-1",
            },
        )

        self.assertRedirects(
            response,
            reverse("cinetrack:buscar") + "?query=Dune",
        )
        self.assertFalse(Contenido.objects.filter(titulo="Dune").exists())

    def test_guardar_desde_busqueda_rechaza_duplicados(self):
        response = self.client.post(
            reverse("cinetrack:guardar_desde_busqueda"),
            {
                "query": "Alien",
                "titulo": self.alien.titulo,
                "tipo": self.alien.tipo,
                "plataforma": self.alien.plataforma,
                "estado": self.alien.estado,
                "veces_vista": "0",
            },
        )

        self.assertRedirects(
            response,
            reverse("cinetrack:buscar") + "?query=Alien",
        )
        self.assertEqual(
            Contenido.objects.filter(titulo=self.alien.titulo).count(),
            1,
        )


@override_settings(
    STORAGES={
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
)
class FavoritosTests(TestCase):
    def setUp(self):
        self.favorita = Contenido.objects.create(
            titulo="Arrival",
            resumen="Primer contacto.",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.PRIME,
            estado=Contenido.Estado.VISTA,
            favorita=True,
        )
        self.otra_favorita = Contenido.objects.create(
            titulo="Dark",
            tipo=Contenido.Tipo.SERIE,
            plataforma=Contenido.Plataforma.NETFLIX,
            estado=Contenido.Estado.VISTA,
            favorita=True,
        )
        self.no_favorita = Contenido.objects.create(
            titulo="Dune",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.HBO,
            estado=Contenido.Estado.PENDIENTE,
            favorita=False,
        )

    def datos_edicion(self, contenido, **cambios):
        datos = {
            "titulo": contenido.titulo,
            "resumen": contenido.resumen,
            "fecha": "",
            "tipo": contenido.tipo,
            "plataforma": contenido.plataforma,
            "calificacion": contenido.calificacion or "",
            "veces_vista": contenido.veces_vista,
            "estado": contenido.estado,
            "volveria_a_ver": "on" if contenido.volveria_a_ver else "",
            "tendra_continuacion": (
                "on" if contenido.tendra_continuacion else ""
            ),
            "favorita": "on" if contenido.favorita else "",
        }
        datos.update(cambios)
        return datos

    def test_lista_exclusivamente_contenidos_favoritos(self):
        response = self.client.get(reverse("cinetrack:favoritos"))
        listados = [
            *response.context["peliculas"],
            *response.context["series"],
        ]

        self.assertEqual(
            {contenido.pk for contenido in listados},
            {self.favorita.pk, self.otra_favorita.pk},
        )
        self.assertNotIn(self.no_favorita, listados)
        self.assertContains(response, "2 títulos")

    def test_muestra_todos_los_favoritos_sin_paginar(self):
        Contenido.objects.bulk_create([
            Contenido(
                titulo=f"Película favorita {indice}",
                tipo=Contenido.Tipo.PELICULA,
                favorita=True,
            )
            for indice in range(30)
        ])
        Contenido.objects.bulk_create([
            Contenido(
                titulo=f"Serie favorita {indice}",
                tipo=Contenido.Tipo.SERIE,
                favorita=True,
            )
            for indice in range(30)
        ])

        response = self.client.get(reverse("cinetrack:favoritos"))

        self.assertEqual(len(response.context["peliculas"]), 31)
        self.assertEqual(len(response.context["series"]), 31)
        self.assertNotContains(response, "Paginación de favoritos")

    def test_estado_vacio(self):
        Contenido.objects.update(favorita=False)

        response = self.client.get(reverse("cinetrack:favoritos"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sin favoritos")
        self.assertEqual(response.context["total_favoritos"], 0)

    def test_tarjetas_enlazan_detalle_con_retorno_completo(self):
        retorno = reverse("cinetrack:favoritos") + "?futuro=valor"
        response = self.client.get(retorno)
        retorno_codificado = quote(retorno, safe="/")

        self.assertContains(
            response,
            reverse("cinetrack:detalle", args=[self.favorita.pk])
            + "?origen=favoritos&amp;return_to="
            + retorno_codificado,
        )

    def test_detalle_regresa_a_favoritos_con_parametros(self):
        retorno = reverse("cinetrack:favoritos") + "?futuro=valor"
        response = self.client.get(
            reverse("cinetrack:detalle", args=[self.favorita.pk])
            + "?origen=favoritos&return_to="
            + quote(retorno, safe=""),
        )

        self.assertEqual(response.context["url_retorno"], retorno)
        self.assertContains(response, "Volver a favoritos")

    def test_tarjetas_enlazan_editar_con_retorno_completo(self):
        retorno = reverse("cinetrack:favoritos") + "?futuro=valor"
        response = self.client.get(retorno)

        self.assertContains(
            response,
            reverse("cinetrack:editar", args=[self.favorita.pk])
            + "?origen=favoritos&amp;return_to="
            + quote(retorno, safe="/"),
        )

    def test_guardar_desde_editar_regresa_a_favoritos(self):
        retorno = reverse("cinetrack:favoritos") + "?futuro=valor"
        response = self.client.post(
            reverse("cinetrack:editar", args=[self.favorita.pk])
            + "?origen=favoritos&return_to="
            + quote(retorno, safe=""),
            self.datos_edicion(self.favorita, resumen="Actualizado."),
        )

        self.assertRedirects(response, retorno)
        self.favorita.refresh_from_db()
        self.assertEqual(self.favorita.resumen, "Actualizado.")

    def test_cancelar_y_volver_desde_editar_conservan_favoritos(self):
        retorno = reverse("cinetrack:favoritos") + "?futuro=valor"
        response = self.client.get(
            reverse("cinetrack:editar", args=[self.favorita.pk])
            + "?origen=favoritos&return_to="
            + quote(retorno, safe=""),
        )

        self.assertEqual(response.context["url_retorno"], retorno)
        self.assertContains(response, f'href="{escape(retorno)}"', count=2)
        self.assertContains(response, "Volver a favoritos")

    def test_quitar_favorito_no_elimina_contenido(self):
        retorno = reverse("cinetrack:favoritos") + "?futuro=valor"
        response = self.client.post(
            reverse("cinetrack:toggle_favorita", args=[self.favorita.pk]),
            {"return_to": retorno},
        )

        self.assertRedirects(response, retorno)
        self.favorita.refresh_from_db()
        self.assertFalse(self.favorita.favorita)
        self.assertTrue(
            Contenido.objects.filter(pk=self.favorita.pk).exists()
        )

    def test_toggle_requiere_post(self):
        response = self.client.get(
            reverse("cinetrack:toggle_favorita", args=[self.favorita.pk])
        )

        self.assertEqual(response.status_code, 405)
        self.favorita.refresh_from_db()
        self.assertTrue(self.favorita.favorita)

    def test_toggle_puede_marcar_un_contenido_como_favorito(self):
        response = self.client.post(
            reverse(
                "cinetrack:toggle_favorita",
                args=[self.no_favorita.pk],
            )
        )

        self.assertRedirects(response, reverse("cinetrack:favoritos"))
        self.no_favorita.refresh_from_db()
        self.assertTrue(self.no_favorita.favorita)

    def test_retorno_externo_no_se_utiliza(self):
        response = self.client.post(
            reverse("cinetrack:toggle_favorita", args=[self.favorita.pk])
            + "?return_to="
            + quote("https://example.com/externo", safe=""),
        )

        self.assertRedirects(response, reverse("cinetrack:favoritos"))

    def test_detalle_y_editar_rechazan_retorno_externo(self):
        externo = "https://example.com/externo"
        fallback = reverse("cinetrack:favoritos")

        detalle = self.client.get(
            reverse("cinetrack:detalle", args=[self.favorita.pk])
            + "?origen=favoritos&return_to="
            + quote(externo, safe=""),
        )
        editar = self.client.get(
            reverse("cinetrack:editar", args=[self.favorita.pk])
            + "?origen=favoritos&return_to="
            + quote(externo, safe=""),
        )

        self.assertEqual(detalle.context["url_retorno"], fallback)
        self.assertEqual(editar.context["url_retorno"], fallback)


@override_settings(
    STORAGES={
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
)
class PortadasTests(TestCase):
    def setUp(self):
        self.contenido = Contenido.objects.create(
            titulo="Blade Runner",
            imagen="/poster/blade-runner.jpg",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.HBO,
            estado=Contenido.Estado.VISTA,
            favorita=True,
        )
        self.secuela = Contenido.objects.create(
            titulo="Blade Runner 2049",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.HBO,
            estado=Contenido.Estado.VISTA,
        )
        self.url_esperada = (
            "https://image.tmdb.org/t/p/w500/poster/blade-runner.jpg"
        )

    def datos_edicion(self):
        return {
            "titulo": self.contenido.titulo,
            "resumen": self.contenido.resumen,
            "fecha": "",
            "tipo": self.contenido.tipo,
            "plataforma": self.contenido.plataforma,
            "calificacion": "",
            "veces_vista": "0",
            "estado": self.contenido.estado,
            "volveria_a_ver": "",
            "tendra_continuacion": "",
            "favorita": "on",
        }

    def test_resolucion_admite_url_absoluta_path_tmdb_y_vacio(self):
        absoluta = "https://example.com/poster.jpg"

        self.assertEqual(resolver_url_portada(absoluta), absoluta)
        self.assertEqual(
            resolver_url_portada("/poster.jpg"),
            "https://image.tmdb.org/t/p/w500/poster.jpg",
        )
        self.assertEqual(resolver_url_portada(""), "")
        self.assertEqual(resolver_url_portada(None), "")

    def test_editar_sin_imagen_conserva_portada_existente(self):
        imagen_original = self.contenido.imagen

        response = self.client.post(
            reverse("cinetrack:editar", args=[self.contenido.pk]),
            self.datos_edicion(),
        )

        self.assertRedirects(
            response,
            reverse("cinetrack:detalle", args=[self.contenido.pk]),
        )
        self.contenido.refresh_from_db()
        self.assertEqual(self.contenido.imagen, imagen_original)

    def test_catalogo_favoritos_y_grupo_resuelven_la_misma_url(self):
        respuestas = (
            self.client.get(reverse("cinetrack:catalogo")),
            self.client.get(reverse("cinetrack:favoritos")),
            self.client.get(
                reverse("cinetrack:grupo_saga", args=["blade runner"])
            ),
        )

        for response in respuestas:
            with self.subTest(path=response.request["PATH_INFO"]):
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, self.url_esperada)

    def test_imagen_vacia_renderiza_placeholder(self):
        contenido = Contenido.objects.create(
            titulo="Sin portada",
            imagen="",
            tipo=Contenido.Tipo.PELICULA,
            plataforma=Contenido.Plataforma.PRIME,
        )

        response = self.client.get(
            reverse("cinetrack:detalle", args=[contenido.pk])
        )

        self.assertContains(response, "Sin imagen")
        self.assertNotContains(response, 'src=""')

    def test_navegacion_y_toggle_no_modifican_imagen(self):
        imagen_original = self.contenido.imagen

        self.client.get(
            reverse("cinetrack:detalle", args=[self.contenido.pk])
        )
        self.client.post(
            reverse(
                "cinetrack:toggle_favorita",
                args=[self.contenido.pk],
            )
        )

        self.contenido.refresh_from_db()
        self.assertEqual(self.contenido.imagen, imagen_original)
