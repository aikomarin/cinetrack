from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from ..content.navigation import obtener_retorno_favoritos
from ..models import Contenido


def favoritos(request):
    favoritos_qs = Contenido.objects.filter(
        favorita=True,
    ).order_by("-updated_at", "-id")
    items = list(favoritos_qs)

    return render(request, "cinetrack/favoritos.html", {
        "top3": items[:3],
        "peliculas": [
            item for item in items
            if item.tipo == Contenido.Tipo.PELICULA
        ],
        "series": [
            item for item in items
            if item.tipo == Contenido.Tipo.SERIE
        ],
        "total_favoritos": len(items),
    })


@require_POST
def toggle_favorita(request, pk):
    contenido = get_object_or_404(Contenido, pk=pk)
    contenido.favorita = not contenido.favorita
    contenido.save(update_fields=["favorita", "updated_at"])

    retorno = obtener_retorno_favoritos(request)
    if retorno:
        return redirect(retorno)

    return redirect(reverse("cinetrack:favoritos"))
