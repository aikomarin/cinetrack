from rest_framework import serializers

from .models import Contenido


class ContenidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenido
        fields = [
            "id",
            "titulo",
            "resumen",
            "imagen",
            "fecha",
            "tipo",
            "plataforma",
            "calificacion",
            "veces_vista",
            "estado",
            "volveria_a_ver",
            "tendra_continuacion",
            "favorita",
            "fase_kanban",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]
