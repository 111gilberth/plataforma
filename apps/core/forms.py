from django.forms import ModelForm
from django import forms

## importamos nuestro modelo creado anteriormente

from .models import Contacto

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['Nombre','Apellido_paterno','Apellido_materno','Correo','phone_number','estados','calle','no_exterior','no_interior','fecha',]
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control','placeholder':"Nombre"}),
            'Apellido_paterno': forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellido Paterno'}),
            'Apellido_materno': forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellido Materno'}),
            'Correo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Correo Electrónico'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control','placeholder':'Telefono'}),
            'estados': forms.TextInput(attrs={'class': 'form-control','placeholder':'Estados'}),
            'calle': forms.TextInput(attrs={'class': 'form-control','placeholder':'Calle'}),
            'no_exterior': forms.TextInput(attrs={'class': 'form-control','placeholder':'Numero exterior'}),
            'no_interior': forms.TextInput(attrs={'class': 'form-control','placeholder':'Numero interior'}),
            'fecha' : forms.DateInput(attrs={'class':'datepicker'}),

                                            
        }
        labels = {
            'Nombre':'','Apellido_paterno':'','Apellido_materno':'','Correo':'','phone_number':'','estados':'','calle':'','no_exterior':'','no_interior':'',
        }

