from django import forms

from ..content.images import resolver_url_portada
from ..content.forms import ContenidoForm
from ..models import Contenido


class CatalogoFiltrosForm(forms.Form):
    tipo = forms.ChoiceField(
        required=False,
        choices=(("", "Todos"), *Contenido.Tipo.choices),
    )
    plataforma = forms.ChoiceField(
        required=False,
        choices=(("", "Todas"), *Contenido.Plataforma.choices),
    )
    estado = forms.ChoiceField(
        required=False,
        choices=(("", "Todos"), *Contenido.Estado.choices),
    )
    favorita = forms.ChoiceField(
        required=False,
        choices=(("", "Todas"), ("1", "Favoritas")),
    )
    volveria_a_ver = forms.ChoiceField(
        required=False,
        choices=(("", "Todas"), ("1", "Volvería a ver")),
    )
    buscar = forms.CharField(required=False, max_length=200)

    def filtros_validos(self):
        if not self.is_bound:
            return {nombre: "" for nombre in self.fields}

        self.is_valid()
        return {
            nombre: self.cleaned_data.get(nombre, "")
            for nombre in self.fields
        }


class ContenidoDesdeBusquedaForm(ContenidoForm):
    """Valida el guardado de TMDB con las mismas reglas del contenido manual."""

    imagen = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
    )

    class Meta(ContenidoForm.Meta):
        fields = [*ContenidoForm.Meta.fields, "imagen"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["plataforma"].required = True

    def clean_imagen(self):
        return resolver_url_portada(self.cleaned_data["imagen"])
