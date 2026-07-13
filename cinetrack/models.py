from django.db import models


class Contenido(models.Model):
    class Tipo(models.TextChoices):
        PELICULA = "pelicula", "Película"
        SERIE = "serie", "Serie"

    class Estado(models.TextChoices):
        VISTA = "vista", "Vista"
        PENDIENTE = "pendiente", "Pendiente"

    class Plataforma(models.TextChoices):
        PRIME = "prime", "Amazon Prime"
        DISNEY = "disney", "Disney+"
        HBO = "hbo", "HBO"
        NETFLIX = "netflix", "Netflix"
        VIX = "vix", "Vix"
        OTRO = "otro", "Otra"

    class Calificacion(models.TextChoices):
        EXCELENTE = "excelente", "Excelente"
        BUENA = "buena", "Buena"
        REGULAR = "regular", "Regular"
        MALA = "mala", "Mala"
        HORRIBLE = "horrible", "Horrible"

    class FaseKanban(models.TextChoices):
        NUEVO = "nuevo", "Nuevo"
        PRONTO = "pronto", "Pronto"
        EN_CURSO = "encurso", "En curso"
        PAUSADO = "pausado", "Pausado"

    # Datos principales
    titulo = models.CharField(max_length=200)
    resumen = models.TextField(blank=True)
    imagen = models.URLField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    # Clasificación
    tipo = models.CharField(max_length=10, choices=Tipo.choices)
    plataforma = models.CharField(
        max_length=20,
        choices=Plataforma.choices,
        blank=True,
    )
    calificacion = models.CharField(
        max_length=10,
        choices=Calificacion.choices,
        blank=True,
        null=True,
    )

    # Seguimiento y preferencias
    veces_vista = models.PositiveIntegerField(default=0)
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.PENDIENTE,
    )
    volveria_a_ver = models.BooleanField(default=False)
    tendra_continuacion = models.BooleanField(default=False)
    favorita = models.BooleanField(default=False)

    # Flujo Kanban
    fase_kanban = models.CharField(
        max_length=12,
        choices=FaseKanban.choices,
        default=FaseKanban.NUEVO,
        db_index=True,
    )

    # Metadatos
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.titulo

    class Meta:
        ordering = ["titulo"]


class SagaAlias(models.Model):
    key = models.CharField(max_length=200, unique=True, db_index=True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]


class Maraton(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(blank=True)
    contenidos = models.ManyToManyField(
        Contenido,
        related_name="maratones",
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        ordering = ["nombre"]
