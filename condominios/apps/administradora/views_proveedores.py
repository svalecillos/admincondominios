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



class ProveedorRegistrarView(SuccessMessageMixin,CreateView):

	form_class = RegistrarProveedorForm
	template_name = 'administrador/registrar_proveedor.html'
	success_message = 'Proveedor registrado con exito'
	success_url = reverse_lazy('administradora_app:proveedorRegistrar')

	def form_valid(self, form):
		form.instance.creadoPor = Usuario.objects.get(pk=self.request.user.id)
		return super(ProveedorRegistrarView, self).form_valid(form)

class ProveedorListarView(ListView):

    template_name = 'administrador/listar_proveedor.html'
    model = Proveedor

    def get_context_data(self, **kwargs):
        context = super(ProveedorListarView, self).get_context_data(**kwargs)
        context['cantidad'] = context['proveedor_list'].count()
        return context

class ProveedorDetalle(DetailView):
 
    queryset = Proveedor.objects.all()
    template_name = 'administrador/detalle_proveedor.html'
 
    def get_object(self):
        # Llamamos a la superclase
        object = super(ProveedorDetalle, self).get_object()
        # Retornamos el objeto
        return object

class ProveedorActualizar(SuccessMessageMixin,UpdateView):
    model = Proveedor
    fields = ['condominio','proveedor','telefono','correo']
    template_name = 'administrador/actualizar_proveedor.html'
    success_message = "Proveedor actualizado con exito"
    success_url = '/proveedor' #listar

class ProveedorEliminar(SuccessMessageMixin,DeleteView):

    template_name = 'administrador/eliminar_proveedor.html'
    model = Proveedor
    success_message = "Proveedor eliminado con exito"
    success_url = '/proveedor'
