from django.db import models
from django import forms
from apps.venezuela.models import *
# Create your models here.

class Condominio(models.Model):
	parroquia = models.ForeignKey(Parroquia)
	condominio = models.CharField(max_length=100)
	ciudad = models.CharField(max_length=100)
	urbanizacion_sector = models.CharField(max_length=80)
	avenida_calle = models.CharField(max_length=150)
	nombre_edificacion = models.CharField(max_length=150)
	correo = models.EmailField()
	telefono = models.CharField(max_length=11)
	class Meta:
		verbose_name_plural = "Condominios"

