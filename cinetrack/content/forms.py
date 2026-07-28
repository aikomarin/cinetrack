from django import forms

from ..models import Contenido


FORM_CONTROL = {"class": "form-control"}
FORM_CHECK = {"class": "form-check-input"}
VIEWING_FIELDS = (
    "calificacion",
    "veces_vista",
    "favorita",
    "volveria_a_ver",
)


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
            "resumen": forms.Textarea(
                attrs={"class": "form-control", "rows": 4}
            ),
            "fecha": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "class": "form-control ct-date-input",
                    "placeholder": "Selecciona una fecha",
                    "autocomplete": "off",
                },
            ),
            "tipo": forms.Select(attrs=FORM_CONTROL),
            "plataforma": forms.Select(attrs=FORM_CONTROL),
            "calificacion": forms.Select(attrs=FORM_CONTROL),
            "veces_vista": forms.NumberInput(
                attrs={"class": "form-control", "min": 0}
            ),
            "estado": forms.Select(attrs=FORM_CONTROL),
            "volveria_a_ver": forms.CheckboxInput(attrs=FORM_CHECK),
            "tendra_continuacion": forms.CheckboxInput(attrs=FORM_CHECK),
            "favorita": forms.CheckboxInput(attrs=FORM_CHECK),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["veces_vista"].required = False
        self.fields["fecha"].input_formats = ["%Y-%m-%d"]
        self.fields["tipo"].choices = self._con_etiqueta_vacia(
            self.fields["tipo"].choices,
            "Selecciona un tipo",
        )
        self.fields["plataforma"].choices = self._con_etiqueta_vacia(
            self.fields["plataforma"].choices,
            "Sin plataforma",
        )
        self.fields["calificacion"].choices = self._con_etiqueta_vacia(
            self.fields["calificacion"].choices,
            "Sin calificación",
        )
        self._configurar_estado_inicial_visionado()

    def _configurar_estado_inicial_visionado(self):
        if self.is_bound:
            estado = self.data.get(self.add_prefix("estado"))
        else:
            estado = self.initial.get(
                "estado",
                Contenido.Estado.PENDIENTE,
            )

        if estado != Contenido.Estado.PENDIENTE:
            return

        self.initial.update(
            calificacion=None,
            veces_vista=0,
            favorita=False,
            volveria_a_ver=False,
        )
        for field_name in VIEWING_FIELDS:
            self.fields[field_name].widget.attrs["disabled"] = True

    @staticmethod
    def _con_etiqueta_vacia(choices, etiqueta):
        return [
            (valor, etiqueta if valor == "" else texto)
            for valor, texto in choices
        ]

    def clean(self):
        cleaned_data = super().clean()
        estado = cleaned_data.get("estado")

        if estado == Contenido.Estado.PENDIENTE:
            for field_name in VIEWING_FIELDS:
                self._errors.pop(field_name, None)
            cleaned_data.update(
                calificacion=None,
                veces_vista=0,
                favorita=False,
                volveria_a_ver=False,
            )
        elif estado == Contenido.Estado.VISTA:
            veces_vista = cleaned_data.get("veces_vista")
            if (
                "veces_vista" not in self.errors
                and (veces_vista is None or veces_vista < 1)
            ):
                self.add_error(
                    "veces_vista",
                    "Un contenido visto debe tener al menos una visualización.",
                )

        titulo = cleaned_data.get("titulo")
        plataforma = cleaned_data.get("plataforma")

        if titulo is None or plataforma is None:
            return cleaned_data

        duplicados = Contenido.objects.filter(
            titulo=titulo,
            plataforma=plataforma,
        )
        if self.instance.pk:
            duplicados = duplicados.exclude(pk=self.instance.pk)

        if duplicados.exists():
            raise forms.ValidationError(
                "Este contenido ya fue registrado previamente."
            )

        return cleaned_data
