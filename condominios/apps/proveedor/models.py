from django.db import models
from apps.condominio.models import *
from apps.usuarios.models import *
from apps.servicio.models import *

class Proveedor(models.Model):

	condominio = models.ForeignKey(Condominio)
	usuario = models.ForeignKey(Usuario)
	proveedor = models.CharField(max_length=100)
	rif = models.CharField(max_length=13)
	estatus = models.BooleanField(default=True)
	servicios_mensuales = models.ManyToManyField(ServicioMensual)
	servicios_especiales = models.ManyToManyField(ServicioEspecial)

	def __str__(self):
		return self.proveedor

	class Meta:
		verbose_name_plural = "Proveedores"


