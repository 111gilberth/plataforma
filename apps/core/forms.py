from django.forms import ModelForm
from django import forms

## importamos nuestro modelo creado anteriormente

from .models import Contacto

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        widgets = {
        	'myfield': forms.TextInput(attrs={'class': 'myfieldclass'})
        }

