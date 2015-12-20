from django.db import models
from apps.venezuela.models import *

class Condominio(models.Model):

	parroquia = models.ForeignKey(Parroquia)
	condominio = models.CharField(max_length=100,unique=True)
	ciudad = models.CharField(max_length=100,null=True)
	urbanizacion_sector = models.CharField(max_length=80)
	avenida_calle = models.CharField(max_length=150)
	nombre_edificacion = models.CharField(max_length=150)
	correo = models.EmailField(null=True)
	telefono = models.CharField(max_length=12,null=True)
	estatus = models.BooleanField(default=True)

	def __str__(self):
		return self.condominio

	class Meta:
		verbose_name_plural = "Condominios"

