from django import forms

from .models import Contenido, Maraton, SagaAlias


FORM_CONTROL = {"class": "form-control"}
FORM_CHECK = {"class": "form-check-input"}


def obtener_contenidos_ordenados():
    return Contenido.objects.order_by("titulo")


class ContenidoForm(forms.ModelForm):
    class Meta:
        model = Contenido
        fields = [
            "titulo",
            "resumen",
            "fecha",
            "tipo",
            "plataforma",
            "calificacion",
            "veces_vista",
            "estado",
            "volveria_a_ver",
            "tendra_continuacion",
            "favorita",
        ]
        widgets = {
            "titulo": forms.TextInput(attrs=FORM_CONTROL),
            "resumen": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "fecha": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "class": "form-control ct-date-input",
                    "placeholder": "Selecciona una fecha",
                    "autocomplete": "off",
                },
            ),
            "tipo": forms.Select(attrs={"class": "form-control"}),
            "plataforma": forms.Select(attrs={"class": "form-control"}),
            "calificacion": forms.Select(attrs={"class": "form-control"}),
            "veces_vista": forms.NumberInput(
                attrs={"class": "form-control", "min": 0}
            ),
            "estado": forms.Select(attrs={"class": "form-control"}),
            "volveria_a_ver": forms.CheckboxInput(attrs=FORM_CHECK),
            "tendra_continuacion": forms.CheckboxInput(attrs=FORM_CHECK),
            "favorita": forms.CheckboxInput(attrs=FORM_CHECK),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fecha"].input_formats = ["%Y-%m-%d"]


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
