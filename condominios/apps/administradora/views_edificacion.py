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


class RegistrarTipoEdificacionView(CreateView):

	form_class = RegistrarTipoEdificacionForm
	template_name = 'administrador/registrar_tipo_edificacion.html'
	success_url = reverse_lazy('administradora_app:tipoEdificacionListar')
	succes_message = "Edificacion registrado con exito"

	def form_valid(self, form):
		return super(RegistrarTipoEdificacionView, self).form_valid(form)

class TipoEdificacionListar(ListView):

    template_name = 'administrador/listar_edificaciones.html'
    model = TipoEdificacion

    def get_context_data(self, **kwargs):
       context = super(TipoEdificacionListar, self).get_context_data(**kwargs)
       context['cantidad'] = context['tipoedificacion_list'].count()
       return context

class TipoEdificacionActualizar(SuccessMessageMixin,UpdateView):
   
    model = TipoEdificacion
    fields = ['edificacion']
    template_name = 'administrador/actualizar_edificacion.html'
    success_message = "Edificacion actualizado con exito"
    success_url = '/edificaciones' #listar

def TipoEdificacionEliminar(request,pk):
    redireccion='/edificaciones'
    sms='Edificacion modificado con exito.'
    template='administrador/eliminar_edificacion.html'
    r=Reutilizable(request,pk,TipoEdificacion,redireccion,sms)


    if request.method != "POST":
        return render(request,template,r.diccionario())
    else:
        return redirect(r.estatus())

