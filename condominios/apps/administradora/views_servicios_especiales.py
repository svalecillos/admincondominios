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



class ServicioEspecialRegistrarView(CreateView):

	form_class = RegistrarServicioEspecialForm
	template_name = 'administrador/registrar_servicio_especial.html'
	success_url = reverse_lazy('administradora_app:servicioEspecialRegistrar')

	def form_valid(self, form):
		form.instance.estatus=True
		return super(ServicioEspecialRegistrarView, self).form_valid(form)

class ServicioEspecialListarView(ListView):

    template_name = 'administrador/listar_servicio_especial.html'
    model = ServicioEspecial

    def get_context_data(self, **kwargs):
        context = super(ServicioEspecialListarView, self).get_context_data(**kwargs)
        context['cantidad'] = context['servicioespecial_list'].count()
        return context

class ServicioEspecialDetalle(DetailView):
 
    queryset = ServicioEspecial.objects.all()
    template_name = 'administrador/detalle_servicio_especial.html'
 
    def get_object(self):
        return super(ServicioEspecialDetalle, self).get_object()

class ServicioEspecialActualizar(SuccessMessageMixin,UpdateView):
    model = ServicioEspecial
    fields = ['condominio','proveedor','servicioEspecial']
    template_name = 'administrador/actualizar_servicio_especial.html'
    success_message = "Servicio actualizado con exito"
    success_url = '/servicioEspecial'

def ServicioEspecialEliminar(request,pk):
	redireccion='/servicioEspecial'
	sms='Servicio modificado con exito.'
	template='administrador/eliminar_servicio_especial.html'
	r=Reutilizable(request,pk,ServicioEspecial,redireccion,sms)


	if request.method != "POST":
		return render(request,template,r.diccionario())
	else:
		return redirect(r.estatus())    