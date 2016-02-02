from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from .models import *
from .forms import *
from django.contrib import messages
"""
Esta funcion imprime en la consola el argumento recibido
es util para 
arg (requerido): Argumento el cual sera impreso en pantalla de consola con print
nombre (opcional): Para mostrar el nombre del Argumento por consola
"""

def ver(arg,nombre=None):
	if arg:
			if nombre :
				print("___________________________________________________________________________")
				print("Debug de: " + nombre)
			print("___________________________________________________________________________\n\n\n")
			print (arg)
			print("\n___________________________________________________________________________\n")


def eliminar(request,pk,modelo):
	if request.method == "POST":
		if request.POST:
			obj=modelo.objects.get(pk=pk)
			if obj.estatus==0:
				obj.estatus=1
				obj.save()
				messages.info(request, 'Servicio reactivado con exito.')
			else:
				obj.estatus=0
				obj.save()
				messages.info(request, 'Servicio desactivado con exito.')				
			return redirect('/servicioMensual')
	else:
		ver(str(modelo.objects.get(pk=pk)))
		return render(request, 'administrador/eliminar_servicio_mensual.html', 
				{str(modelo.__name__) : modelo.objects.get(pk=pk)})  


class Reutilizable(object):

	def __init__(self, request,pk,modelo,redireccion,sms):
		self.peticion=request
		self.id=pk
		self.modelo=modelo
		self.redireccion=redireccion
		self.sms=sms

	def estatus(self):

		obj=self.modelo.objects.get(pk=self.id)
		if obj.estatus==0:
			obj.estatus=1
			obj.save()
			messages.info(self.peticion, self.sms)
		else:
			obj.estatus=0
			obj.save()
			messages.info(self.peticion, self.sms)		
		return self.redireccion;

	def diccionario(self):
			return {str(self.modelo.__name__) : self.modelo.objects.get(pk=self.id)}
	