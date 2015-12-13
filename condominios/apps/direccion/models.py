from django.db import models
from django.template.defaultfilters import slugify

from django.conf import settings

# Create your models here.

class TimeStampModel(models.Model):
	
	creacion = models.DateTimeField(auto_now_add=True)
	modificacion= models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class Estados(models.Model):

	estado = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.estado
	estado.short_description = 'Es Estado'

class Municipios(models.Model):

	estado = models.ForeignKey(Estados)
	municipio = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.municipio
	estado.short_description = 'Es Estado'
	municipio.short_description = 'Es Municipio'

class Parroquias(models.Model):

	municipio = models.ForeignKey(Municipios)
	parroquia = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.parroquia