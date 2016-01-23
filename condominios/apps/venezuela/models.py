# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from apps.usuarios.models import *

from django.conf import settings

class Estado(models.Model):
    estado = models.CharField(max_length=50)
    iso_3166_2 = models.CharField(max_length=5)

    def __str__(self):
        return str(self.estado.encode('utf-8'))

    class Meta:
        verbose_name = u'Estado'
        verbose_name_plural = u'Estados'


class Ciudad(models.Model):
    estado = models.ForeignKey('Estado')
    ciudad = models.CharField(max_length=100)
    capital = models.IntegerField(default=0)

    def __str__(self):
        return str(self.ciudad.encode('utf-8'))

    class Meta:
        verbose_name = u'Ciudad'
        verbose_name_plural = u'Ciudades'


class Municipio(models.Model):
    estado = models.ForeignKey('Estado')
    municipio = models.CharField(max_length=100)

    def __str__(self):
        return str(self.municipio.encode('utf-8'))

    class Meta:
        verbose_name = u'Municipio'
        verbose_name_plural = u'Municipios'


class Parroquia(models.Model):
    municipio = models.ForeignKey('Municipio')
    parroquia = models.CharField(max_length=100)

    def __str__(self):
        return str(self.parroquia.encode('utf-8'))

    class Meta:
        verbose_name = u'Parroquía'
        verbose_name_plural = u'Parroquías'

class PrefijoTelefonico(models.Model):
    
    municipio = models.ForeignKey(Municipio)
    prefijo = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.prefijo)

    class Meta:
        verbose_name = u'Prefijo telefonico'
        verbose_name_plural = u'Prefijos telefonicos'

class prefijoCelular(models.Model):
    
    prefijo = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.prefijo)
        
    class Meta:
        verbose_name = u'Prefijo celular'
        verbose_name_plural = u'Prefijos celulares'

class Banco(models.Model):
    
    banco=models.CharField(max_length=100,unique=True)
    estatus = models.BooleanField(default=True)
    prefijoTarjeta=models.PositiveSmallIntegerField()
    prefijoCuenta=models.PositiveSmallIntegerField()
    creadoPor = models.ForeignKey(Usuario)

    def __str__(self):
        return str(self.banco)
        
    class Meta:
        verbose_name = u'Banco'
        verbose_name_plural = u'Bancos'