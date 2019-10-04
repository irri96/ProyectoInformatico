from Core.models import Estacionamiento
from django import forms

class CrearForm(forms.ModelForm):
    class Meta:
        model = Estacionamiento
        fields = ('lat','lon')