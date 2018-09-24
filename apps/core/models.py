from django.db import models

from django.contrib.auth.models import User

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
