from Core.models import Estacionamiento
from django import forms

class CrearForm(forms.ModelForm):
    calle = forms.CharField()
    class Meta:
        model = Estacionamiento
        fields = ('lat','lon')
        labels = {
            'calle' : 'Calle'
        }