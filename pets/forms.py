from myproject.zoo.models import *
from django import forms
from django.forms import ModelForm
from django.forms import ValidationError
from django.forms import ModelMultipleChoiceField

class SearchForm(forms.Form):
    especie = forms.ChoiceField(
        choices=ESPECIE
    )

    tipo = forms.ChoiceField(
        choices=TIPO
    )


class MascotaForm(ModelForm):

    def clean_telefono(self):
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        telefono = self.cleaned_data.get('telefono')
        for letra in telefono:
            if not letra in numbers:
                raise ValidationError('Telefono Incorrecto (solo numeros)')
        return telefono

    class Meta:
        model = Mascota
        exclude =('usuario',)

class AdoptanteForm(ModelForm):
    mascota = ModelMultipleChoiceField(queryset=MascotaZoonosis.objects.filter(adoptado=False))

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if len(str(dni)) > 10:
            raise ValidationError('DNI Incorecto (maximo 10 numeros)')
        return dni

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if len(str(telefono)) > 11:
            raise ValidationError('Telefono Incorecto (maximo 10 numeros)')
        return telefono

    class Meta:
        model = AdoptanteZoonosis
