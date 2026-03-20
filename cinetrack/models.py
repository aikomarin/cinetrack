from django.db import models


class Contenido(models.Model):
    TIPOS = [
        ("pelicula", "Película"),
        ("serie", "Serie"),
    ]

    ESTADOS = [
        ("vista", "Vista"),
        ("pendiente", "Pendiente"),
    ]

    PLATAFORMAS = [
        ("prime", "Amazon Prime"),
        ("disney", "Disney+"),
        ("hbo", "HBO Max"),
        ("netflix", "Netflix"),
        ("star", "Star+"),
        ("vix", "Vix"),
        ("otro", "Otra"),
    ]

    CALIFICACIONES = [
        ("excelente", "Excelente"),
        ("buena", "Buena"),
        ("regular", "Regular"),
        ("mala", "Mala"),
        ("horrible", "Horrible"),
    ]

    FASES_KANBAN = [
        ("nuevo", "Nuevo"),
        ("pronto", "Pronto"),
        ("encurso", "En curso"),
        ("pausado", "Pausado"),
    ]

    # Datos principales
    titulo = models.CharField(max_length=200)
    resumen = models.TextField(blank=True)
    imagen = models.URLField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    # Clasificación
    tipo = models.CharField(max_length=10, choices=TIPOS)
    plataforma = models.CharField(max_length=20, choices=PLATAFORMAS, blank=True)
    calificacion = models.CharField(
        max_length=10,
        choices=CALIFICACIONES,
        blank=True,
        null=True,
    )
    veces_vista = models.IntegerField(default=0)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="pendiente",
    )
    volveria_a_ver = models.BooleanField(default=False)
    tendra_continuacion = models.BooleanField(default=False)
    favorita = models.BooleanField(default=False)

    # Metadatos / flujo
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    fase_kanban = models.CharField(
        max_length=12,
        choices=FASES_KANBAN,
        default="nuevo",
        db_index=True,
    )

    def __str__(self) -> str:
        return str(self.titulo)


class SagaAlias(models.Model):
    key = models.CharField(max_length=200, unique=True, db_index=True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} ({self.key})"


class Maraton(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(blank=True)
    contenidos = models.ManyToManyField("Contenido", related_name="maratones", blank=True)

    # Metadatos / flujo
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
