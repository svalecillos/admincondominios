from django.db import models
from apps.condominio.models import *

class ServicioEspecial(models.Model):

	condominio = models.ManyToManyField(Condominio)
	servicio_especial = models.CharField(max_length=50,null=True)
	estatus = models.BooleanField(default=True)

	def __str__(self):
		return self.servicio_especial

	class Meta:
		verbose_name_plural = "Servicios especiales"

class ServicioMensual(models.Model):

	condominio = models.ManyToManyField(Condominio)
	servicio_mensual = models.CharField(max_length=50,null=True)
	estatus = models.BooleanField(default=True)

	def __str__(self):
		return self.servicio_mensual

	class Meta:
		verbose_name_plural = "Servicios mensuales"		