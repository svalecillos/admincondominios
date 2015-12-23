from django.db import models
from apps.venezuela.models import *
from apps.usuarios.models import *


class TipoEdificacion(models.Model):

	edificacion = models.CharField(max_length=80)
	estatus = models.BooleanField(default=True)

	def __str__(self):
		return self.edificacion

	#def __iter__(self):
	#	return (self.edificacion)

	class Meta:
		verbose_name_plural = "Edificaciones"

class Condominio(models.Model):
	
	condominio = models.CharField(max_length=100,unique=True)
	rif = models.CharField(max_length=13,blank=True, null=True)
	telefono = models.CharField(max_length=12,null=True,default='')
	correo = models.EmailField(null=True)
	parroquia = models.ForeignKey(Parroquia)
	ciudad  = models.ForeignKey(Ciudad)
	avenidaCalle = models.CharField(max_length=150)
	urbanizacionSector = models.CharField(max_length=80)
	tipoEdificacion = models.ForeignKey(TipoEdificacion,null=True)
	nombreEdificacion = models.CharField(max_length=150,null=True)
	estatus = models.BooleanField(default=True)
	creadoPor = models.ForeignKey(Usuario)


	def __str__(self):
		return self.condominio

	class Meta:
		verbose_name_plural = "Condominios"

class Proveedor(models.Model):

	proveedor = models.CharField(max_length=100)
	rif = models.CharField(max_length=13,blank=True, null=True)
	telefono = models.CharField(max_length=12,null=True)	
	correo = models.EmailField(null=True)
	condominio = models.ForeignKey(Condominio)
	creadoPor = models.ForeignKey(Usuario)

	def __str__(self):
		return self.proveedor

	class Meta:
		verbose_name_plural = "Proveedores"

class ServicioMensual(models.Model):

	condominio = models.ForeignKey(Condominio)
	proveedor = models.ForeignKey(Proveedor)
	servicioMensual = models.CharField(max_length=50,null=True)
	estatus = models.BooleanField(default=True)

	def __str__(self):
		return self.servicioMensual

	class Meta:
		verbose_name_plural = "Servicios mensuales"

class CostoServicioMensual(models.Model):

	costo = models.DecimalField(max_digits=10, decimal_places=2)
	fecha = models.DateTimeField(auto_now=True)
	condominio = models.ForeignKey(Condominio)
	servicioMensual = models.ForeignKey(ServicioMensual)

	def __str__(self):
		return self.servicioMensual.servicioMensual

	class Meta:
		verbose_name_plural = "Costo de servicio mensuales"

class CargoServicioMensual(models.Model):

	monto = models.DecimalField(max_digits=10, decimal_places=2)
	fecha = models.DateTimeField(auto_now=True)
	condominio = models.ForeignKey(Condominio)
	proveedor = models.ForeignKey(Proveedor)
	servicioMensual = models.ForeignKey(ServicioMensual)
	creadoPor = models.ForeignKey(Usuario)

	def __str__(self):
		return self.monto

	class Meta:
		verbose_name_plural = "Cargo servicios mensuales"

class ServicioEspecial(models.Model):

	condominio = models.ForeignKey(Condominio)
	proveedor = models.ForeignKey(Proveedor)
	servicioEspecial = models.CharField(max_length=50,null=True)
	estatus = models.BooleanField(default=True)

	def __str__(self):
		return self.servicioEspecial

	class Meta:
		verbose_name_plural = "Servicios especiales"

class CostoServicioEspecial(models.Model):

	costo = models.DecimalField(max_digits=10, decimal_places=2)
	cuota = models.PositiveSmallIntegerField()
	fecha = models.DateTimeField(auto_now=True)
	condominio = models.ForeignKey(Condominio)
	servicioEspecial = models.ForeignKey(ServicioEspecial)

	def __str__(self):
		return self.servicoEspecial.servicoEspecial

	class Meta:
		verbose_name_plural = "Costo de servicios especiales"

class CargoServicioEspecial(models.Model):

	monto = models.DecimalField(max_digits=10, decimal_places=2)
	fecha = models.DateTimeField(auto_now=True)
	condominio = models.ForeignKey(Condominio)
	proveedor = models.ForeignKey(Proveedor)
	servicioEspecial = models.ForeignKey(ServicioEspecial)
	creadoPor = models.ForeignKey(Usuario)

	def __str__(self):
		return self.monto

	class Meta:
		verbose_name_plural = "Cargo servicios especiales"

class CuentaCondominio(models.Model):

	condominio = models.OneToOneField(Condominio)
	saldo = models.DecimalField(max_digits=10, decimal_places=2)
	fecha = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.condominio.condominio

	class Meta:
		verbose_name_plural = "Cuenta de condominios"

class CuentaUsuario(models.Model):

	usuario = models.OneToOneField(Usuario)
	saldo = models.DecimalField(max_digits=10, decimal_places=2)
	fecha = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.usuario.nombre + " " + self.usuario.apellido

	class Meta:
		verbose_name_plural = "Cuenta de usuarios"

class Transaccion(models.Model):

	CuentaUsuario = models.ForeignKey(CuentaUsuario)
	CuentaCondominio = models.ForeignKey(CuentaCondominio)
	debito = models.DecimalField(max_digits=10, decimal_places=5,blank=True,null=True)
	credito = models.DecimalField(max_digits=10, decimal_places=5,blank=True,null=True)
	descripcion = models.CharField(max_length=80)
	fecha = models.DateTimeField(auto_now=True)
	aprobado = models.BooleanField(default=True)

	def save(self):
		super (Transaccion, self).save()

	def __str__(self):
		return str(self.fecha)

	class Meta:
		verbose_name_plural = "Transacciones"

