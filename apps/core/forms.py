from django.forms import ModelForm
from django import forms

## importamos nuestro modelo creado anteriormente

from .models import Contacto

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['Nombre','Apellido_paterno','Apellido_materno','Correo']
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control','placeholder':"Nombre"}),
            'Apellido_paterno': forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellido Paterno'}),
            'Apellido_materno': forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellido Materno'}),
            'Correo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Correo Electrónico'}),
           
        }
        labels = {
            'Nombre':'','Apellido_paterno':'','Apellido_materno':'','Correo':'',
        }

