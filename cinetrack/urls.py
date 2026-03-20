from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ContenidoViewSet

app_name = "cinetrack"

router = DefaultRouter()
router.register(r"contenidos", ContenidoViewSet)

urlpatterns = [
    # Home / Catálogo / Detalle
    path("", views.home, name="home"),
    path("catalogo/", views.catalogo, name="catalogo"),
    path("detalle/<int:pk>/", views.detalle, name="detalle"),

    # CRUD
    path("registrar/", views.registrar, name="registrar"),
    path("editar/<int:pk>/", views.editar, name="editar"),
    path("eliminar/<int:pk>/", views.eliminar, name="eliminar"),

    # Búsqueda
    path("buscar/", views.buscar, name="buscar"),
    path("guardar-desde-busqueda/", views.guardar_desde_busqueda, name="guardar_desde_busqueda"),

    # Agrupaciones / Sagas
    path("grupo/<path:clave>/", views.grupo_saga, name="grupo_saga"),
    path("sagas/renombrar/", views.renombrar_saga, name="renombrar_saga"),

    # Kanban (Pendientes)
    path("pendientes/", views.pendientes, name="pendientes"),
    path("pendientes/mover/<int:pk>/", views.mover_fase, name="mover_fase"),
    path("pendientes/marcar-vista/<int:pk>/", views.marcar_vista, name="marcar_vista"),

    # Favoritos
    path("favoritos/", views.favoritos, name="favoritos"),
    path("favoritos/toggle/<int:pk>/", views.toggle_favorita, name="toggle_favorita"),

    # Rewatch
    path("volverias/", views.volverias, name="volverias"),

    # Maratón
    path("maratones/", views.maratones, name="maratones"),
    path("maratones/crear/", views.crear_maraton, name="crear_maraton"),
    path("maratones/<int:pk>/", views.detalle_maraton, name="detalle_maraton"),
    path("maratones/<int:pk>/editar/", views.editar_maraton, name="editar_maraton"),
    path("maratones/<int:pk>/eliminar/", views.eliminar_maraton, name="eliminar_maraton"),
    path("maratones/<int:pk>/quitar/<int:contenido_id>/", views.quitar_de_maraton, name="quitar_de_maraton"),

    # API
    path("api/", include(router.urls)),
]
