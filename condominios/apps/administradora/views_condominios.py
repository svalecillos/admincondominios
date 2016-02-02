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

class CondominioRegistrarView(SuccessMessageMixin,CreateView):

    form_class = RegistrarCondominioForm
    template_name = 'administrador/registrar_condominio.html'
    success_url = reverse_lazy('administradora_app:condominioRegistrar')
    success_message = "Condominio creado con exito"

    def form_valid(self, form):
        form.instance.creadoPor = Usuario.objects.get(pk=self.request.user.id)
        form.instance.estatus=True
        return super(CondominioRegistrarView, self).form_valid(form)

        def form_invalid(self, form):
            response = super(CondominioRegistrarView, self).form_invalid(form)
            if self.request.is_ajax():
                return JsonResponse(form.errors, status=400)
            else:
                ver(form.errors,'form.errors')
                return response

        def get_context_data(self,**kwargs):
            context = super(CondominioRegistrarView, self).get_context_data(**kwargs)
            return context 
		
class CondominioListarView(ListView):

    template_name = 'administrador/listar_condominio.html'
    model = Condominio

    def get_context_data(self, **kwargs):
        context = super(CondominioListarView, self).get_context_data(**kwargs)
        context['cantidad'] = context['condominio_list'].count()
        return context

class CondominioDetalle(DetailView):
 
    queryset = Condominio.objects.all()
    template_name = 'administrador/detalle_condominio.html'
 
    def get_object(self):
        # Llamamos a la superclase
        object = super(CondominioDetalle, self).get_object()
        # Retornamos el objeto
        return object

class CondominioActualizar(SuccessMessageMixin,UpdateView):
    model = Condominio
    fields = ['condominio','rif','telefono','correo','avenidaCalle','urbanizacionSector','nombreEdificacion']
    template_name = 'administrador/actualizar_condominio.html'
    success_message = "Condominio actualizado con exito"
    success_url = '/condominio' #listar


def CondominioEliminar(request,pk):
    redireccion='/condominio'
    sms='Condominio modificado con exito.'
    template='administrador/eliminar_condominio.html'
    r=Reutilizable(request,pk,Condominio,redireccion,sms)


    if request.method != "POST":
        return render(request,template,r.diccionario())
    else:
        return redirect(r.estatus())