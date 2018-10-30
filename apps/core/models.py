from django.db import models
import datetime

from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Post(models.Model):
	title = models.CharField(max_length=20, verbose_name='Titulo')#Campo de string corto
	body = models.TextField(verbose_name='Cuerpo')		#cadena de caracteres mas larga, textarea
	img = models.ImageField(verbose_name='Foto') #

	#timestamp
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	autor = models.ForeignKey(User, related_name='autor_del_post', on_delete=models.CASCADE) #campo contenedor de la relacion

class Contacto(models.Model):
    Nombre = models.CharField(max_length=180,verbose_name="Nombre")
    Apellido_paterno = models.CharField(max_length=90,verbose_name="Apellido Paterno")
    Apellido_materno = models.CharField(max_length=90,verbose_name="Apellido Materno")
    Correo = models.EmailField(max_length=254,verbose_name="Correo Electrónico")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El numero de telefono debe ser ingresado de la siguiente manera: '+999999999'. Máximo 15 digitos son aceptados.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17,blank=True) # validators should be a list

    nom_negocio = models.CharField(max_length=90,verbose_name="Nombre del negocio",default='lol')
    cod_postal = models.CharField(max_length=90,verbose_name="Código postal",default="H1W 3J3")
    colonia = models.CharField(max_length=90,verbose_name="Colonia",default="colonia")
    municipio = models.CharField(max_length=90,verbose_name="Municipio",default='municipio')
    estados = models.CharField(max_length=90,verbose_name="Estado",default="Estados")
    calle = models.CharField(max_length=90,verbose_name="Calle",default="Calle")
    no_interior = models.CharField(max_length=90,verbose_name="Numero interior",default="Numero interior")
    no_exterior = models.CharField(max_length=90,verbose_name="Numero exterior",default="Numero exterior")
    fecha = models.DateField(default=datetime.date.today)
    
    class Meta:
        verbose_name = "Contactos registrados por medio del formulario"
    def __str__(self):
        return '%s %s' % (self.Nombre, self.Apellido_paterno)
