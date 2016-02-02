from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from apps.usuarios.models import Usuario
from .models import *
from .forms import *
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.contrib import messages
from .utiles import *


class ServicioMensualRegistrarView(SuccessMessageMixin,CreateView):

	form_class = RegistrarServicioMensualForm
	template_name = 'administrador/registrar_servicio_mensual.html'
	success_url = reverse_lazy('administradora_app:servicioMensualRegistrar')
	success_message='Servicio asociado exitosamente'

	def form_valid(self, form):
		return super(ServicioMensualRegistrarView, self).form_valid(form)

class ServicioMensualListarView(ListView):

    template_name = 'administrador/listar_servicio_mensual.html'
    model = ServicioMensual
    #queryset = ServicioMensual.objects.filter(estatus=1) #donde el servico este activo

    def get_context_data(self, **kwargs):
        context = super(ServicioMensualListarView, self).get_context_data(**kwargs)
        context['cantidad'] = context['serviciomensual_list'].count()
        return context

class ServicioMensualDetalle(DetailView):
 
    queryset = ServicioMensual.objects.all()
    template_name = 'administrador/detalle_servicio_mensual.html'
 
    def get_object(self):
        sm = super(ServicioMensualDetalle, self).get_object()
        return sm

class ServicioMensualActualizar(SuccessMessageMixin,UpdateView):
    model = ServicioMensual
    fields = ['condominio','proveedor','servicioMensual']
    template_name = 'administrador/actualizar_servicio_mensual.html'
    success_message = "Servicio actualizado con exito"
    success_url = '/servicioMensual' #listar
 

def ServicioMensualEliminar(request,pk):
	redireccion='/servicioMensual'
	sms='Servicio modificado con exito.'
	template='administrador/eliminar_servicio_mensual.html'
	r=Reutilizable(request,pk,ServicioMensual,redireccion,sms)


	if request.method != "POST":
		return render(request,template,r.diccionario())
	else:
		return redirect(r.estatus())