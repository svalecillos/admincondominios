# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify

from django.conf import settings

class Estado(models.Model):
    estado = models.CharField(max_length=50)
    iso_3166_2 = models.CharField(max_length=5)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = u'Estado'
        verbose_name_plural = u'Estados'


class Ciudad(models.Model):
    estado = models.ForeignKey('Estado')
    ciudad = models.CharField(max_length=100)
    capital = models.IntegerField(default=0)

    def __str__(self):
        return self.ciudad

    class Meta:
        verbose_name = u'Ciudad'
        verbose_name_plural = u'Ciudades'


class Municipio(models.Model):
    estado = models.ForeignKey('Estado')
    municipio = models.CharField(max_length=100)

    def __str__(self):
        return self.municipio

    class Meta:
        verbose_name = u'Municipio'
        verbose_name_plural = u'Municipios'


class Parroquia(models.Model):
    municipio = models.ForeignKey('Municipio')
    parroquia = models.CharField(max_length=100)

    def __str__(self):
        return self.parroquia

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