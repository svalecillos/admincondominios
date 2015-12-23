from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager, models.Manager):

	def _create_user(self, usuario, cedula, nombre, apellido, correo, password, is_staff, is_superuser, **extra_fields):

		correo = self.normalize_email(correo)
		if not correo:
			raise ValueError('El correo es obligatorio')
		usuario = self.model(
			usuario=usuario,
			cedula=cedula,
			nombre=nombre,
			apellido=apellido,
			correo=correo,
			is_active=True,
			is_staff=is_staff,
			is_superuser=is_superuser,
			**extra_fields)

		usuario.set_password(password)
		usuario.save( using = self._db)
		return usuario
		
	def create_user(self, usuario, cedula, nombre, apellido, correo, password=None, **extra_fields):
		return self._create_user(usuario, cedula, nombre, apellido, correo, password, False, False, **extra_fields)

	def create_superuser(self, usuario, cedula, nombre, apellido, correo, password=None, **extra_fields):
		return self._create_user(usuario, cedula, nombre, apellido, correo, password, True, True, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):

	usuario = models.CharField(max_length=50,unique=True)
	cedula = models.PositiveIntegerField()
	nombre = models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	correo = models.EmailField()
	telefono_habitacion = models.CharField(max_length=12,null=True)
	telefono_movil = models.CharField(max_length=12,null=True)
	numero_vivienda = models.CharField(max_length=5)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserManager()
	USERNAME_FIELD ='usuario'
	REQUIRED_FIELDS =['cedula','nombre','apellido','correo']

	def __str__(self):
		return self.nombre + " " + self.apellido
	def get_short_name(self):
		return self.usuario

