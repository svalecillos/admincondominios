from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from apps.usuarios.models import Usuario
from .models import *
import base64
from .forms import *
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse

# Modificar a CreateView

def registrar_pago(request):
	# if request.method == "POST":
	# 	form = RegistrarCondominioForm(request.POST)
	# 	if form.is_valid():
	# 		return redirect('/')
	# else:
	# 	formulario = RegistrarCondominioForm()
	# return render(request, 'propietario/registrar_pago.html',{'formulario' : formulario})
	return render(request, 'propietario/registrar_pago.html')

# Requiere datos de distintos modelos

def historial_movimientos(request):
	# if request.method == "POST":
	# 	form = RegistrarCondominioForm(request.POST)
	# 	if form.is_valid():
	# 		return redirect('/')
	# else:
	# 	formulario = RegistrarCondominioForm()
	# return render(request, 'condominio.html', 
	# 			{'formulario' : formulario,
	# 			'prueba': tuple(TipoEdificacion.objects.all())})
	return render(request, 'propietario/historial_movimientos.html')


class CondominioRegistrarView(SuccessMessageMixin,CreateView):

	form_class = RegistrarCondominioForm
	template_name = 'condominio/registrar.html'
	success_url = reverse_lazy('administradora_app:condominioRegistrar')
	success_message = "Condominio creado con exito"

	def form_valid(self, form):
		form.instance.creadoPor = Usuario.objects.get(pk=self.request.user.id)
		return super(CondominioRegistrarView, self).form_valid(form)

	def get_context_data(self,**kwargs):
		context = super(CondominioRegistrarView, self).get_context_data(**kwargs)
		return context 


def condominio_old(request):
	if request.method == "POST":
		form = RegistrarCondominioForm(request.POST)
		if form.is_valid():
			return redirect('/')
	else:
		formulario = RegistrarCondominioForm()
	return render(request, 'condominio.html', 
				{'formulario' : formulario,
				'prueba': tuple(TipoEdificacion.objects.all())})


class ProveedorRegistrarView(CreateView):

	form_class = RegistrarProveedorForm
	template_name = 'proveedor/registrar.html'
	success_url = reverse_lazy('administradora_app:proveedorRegistrar')

	def form_valid(self, form):
		form.instance.creadoPor = Usuario.objects.get(pk=self.request.user.id)
		return super(ProveedorRegistrarView, self).form_valid(form)

def proveedor(request):
	if request.method == "POST":
		form = RegistrarProveedorForm(request.POST)
		if form.is_valid():
			form.creadoPor=2
			salvar=form.save()
			#salvar.save()
		return redirect('/')
	else:
		formulario = RegistrarProveedorForm()
	return render(request, 'proveedor.html', 
				{'formulario' : formulario})

class ServicioMensualRegistrarView(CreateView):

	form_class = RegistrarServicioMensualForm
	template_name = 'servicio mensual/registrar.html'
	success_url = reverse_lazy('administradora_app:servicioMensualRegistrar')

	def form_valid(self, form):
		return super(ServicioMensualRegistrarView, self).form_valid(form)

class ServicioEspecialRegistrarView(CreateView):

	form_class = RegistrarServicioEspecialForm
	template_name = 'servicio especial/registrar.html'
	success_url = reverse_lazy('administradora_app:servicioEspecialRegistrar')

	def form_valid(self, form):
		print("\n")
		print("\n--------------------------------------------------\n")
		print(self.request.POST)
		return super(ServicioEspecialRegistrarView, self).form_valid(form)		

class CostoServicioEspecialRegistrarView(CreateView):
	form_class = CostoServicioEspecialRegistrarForm
	template_name = 'costo servicio especial/registrar.html'
	success_url = reverse_lazy('administradora_app:costoServicioEspecialRegistrar')

	def form_valid(self, form):
		return super(CostoServicioEspecialRegistrarView, self).form_valid(form)


class CostoServicioMensualRegistrarView(CreateView):
	form_class = CostoServicioMensualRegistrarForm
	template_name = 'costo servicio mensual/registrar.html'
	success_url = reverse_lazy('administradora_app:costoServicioMensualRegistrar')

	def form_valid(self, form):
		return super(CostoServicioMensualRegistrarView, self).form_valid(form)


class CondominioListarView(ListView):

    template_name = 'condominio/listar.html'
    model = Condominio

    def get_context_data(self, **kwargs):
        context = super(CondominioListarView, self).get_context_data(**kwargs)
        context['b64id']=base64.b64encode(Condominio.id)
        return context

class CondominioDetailView(DetailView):
 
    queryset = Condominio.objects.all()
    template_name = 'condominio/detalle.html'
 
    def get_object(self):
        # Llamamos a la superclase
        object = super(CondominioDetailView, self).get_object()
        # Retornamos el objeto
        return object

class RegistrarCondominioGuiadoView(CreateView):
	form_class = RegistrarCondominioForm
	template_name = 'administrador/registrar_condominio_guiado.html'
	success_url = reverse_lazy('usuarios_app:index')
	initial = {'condominio': 'defecto'}
	def form_valid(self, form):
		return super(RegistrarCondominioGuiadoView, self).form_valid(form)        

def RegistrarCondominioGuiadoView(request):
	if request.method == "POST":
		form_condominio = RegistrarCondominioForm(request.POST)
		if form_condominio.is_valid():
			form_condominio.instance.creadoPor = Usuario.objects.get(pk=self.request.user.id)
			form_condominio.save()
			#salvar.save()
		return redirect('/')
	else:
		formulario = RegistrarCondominioForm()
	return render(request, 'administrador/registrar_condominio_guiado.html', 
				{'form' : formulario})


class RegistrarTipoEdificacionView(CreateView):
	form_class = RegistrarTipoEdificacionForm
	template_name = 'administrador/registrar_tipo_edificacion.html'
	success_url = reverse_lazy('usuarios_app:index')

	def get(self, request,popup):
		if popup is not None:
			return render(request, 'administrador/registrar_tipo_edificacion_popup.html', {'form': self.form_class})
		else:
			return render(request, self.template_name, {'form': self.form_class})

	def form_valid(self, form):
		return super(RegistrarTipoEdificacionView, self).form_valid(form)


