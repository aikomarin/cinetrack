from django.db import migrations


def star_to_disney(apps, schema_editor):
    Contenido = apps.get_model("cinetrack", "Contenido")
    Contenido.objects.filter(plataforma="star").update(plataforma="disney")


def disney_to_star(apps, schema_editor):
    Contenido = apps.get_model("cinetrack", "Contenido")
    Contenido.objects.filter(plataforma="disney").update(plataforma="star")


class Migration(migrations.Migration):

    dependencies = [
        ("cinetrack", "0007_alter_contenido_veces_vista"),
    ]

    operations = [
        migrations.RunPython(star_to_disney, disney_to_star),
    ]