from django import forms

from .content.forms import ContenidoForm
from .models import Contenido, Maraton, SagaAlias


FORM_CONTROL = {"class": "form-control"}


def obtener_contenidos_ordenados():
    return Contenido.objects.order_by("titulo")


class BuscarContenidoForm(forms.Form):
    query = forms.CharField(
        label="Buscar película o serie",
        max_length=100,
        widget=forms.TextInput(attrs=FORM_CONTROL),
    )


class SagaAliasForm(forms.ModelForm):
    class Meta:
        model = SagaAlias
        fields = ["key", "nombre"]
        widgets = {
            "key": forms.HiddenInput(),
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre de la saga",
                }
            ),
        }


class MaratonForm(forms.ModelForm):
    class Meta:
        model = Maraton
        fields = ["nombre", "descripcion", "contenidos"]
        widgets = {
            "nombre": forms.TextInput(attrs=FORM_CONTROL),
            "descripcion": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
            "contenidos": forms.SelectMultiple(
                attrs={"class": "form-select"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["contenidos"].queryset = obtener_contenidos_ordenados()
