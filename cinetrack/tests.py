from urllib.parse import quote

from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils.html import escape

from .models import Contenido


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
