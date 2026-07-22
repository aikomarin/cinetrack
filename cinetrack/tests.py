from urllib.parse import quote

from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils.html import escape

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
