from django import forms
from .models import Contenido, SagaAlias, Maraton


class ContenidoForm(forms.ModelForm):
    class Meta:
        model = Contenido
        fields = [
            'titulo', 'tipo', 'plataforma', 'calificacion', 'veces_vista',
            'volveria_a_ver', 'estado', 'tendra_continuacion', 'favorita'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'plataforma': forms.Select(attrs={'class': 'form-control'}),
            'calificacion': forms.Select(attrs={'class': 'form-control'}),
            'veces_vista': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'volveria_a_ver': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tendra_continuacion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'favorita': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class BuscarContenidoForm(forms.Form):
    query = forms.CharField(
        label='Buscar película o serie',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


class SagaAliasForm(forms.ModelForm):
    class Meta:
        model = SagaAlias
        fields = ['key', 'nombre']
        widgets = {
            'key': forms.HiddenInput(),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la saga'}),
        }


class MaratonForm(forms.ModelForm):
    class Meta:
        model = Maraton
        fields = ["nombre", "descripcion", "contenidos"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "contenidos": forms.SelectMultiple(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["contenidos"].queryset = Contenido.objects.order_by("titulo")
