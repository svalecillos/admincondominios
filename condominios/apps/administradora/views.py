from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from apps.usuarios.models import Usuario
from .models import *
from .forms import *
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.contrib import messages
#from sertiven.utiles import ver
from .utiles import *

@login_required()
def inicio(request):
	#if request.method == "POST":
		# if 'register_form' in request.POST:

		# 	login_form = LoginForm(request.POST)
		# 	if login_form.is_valid():
		# 		LogIn(request, login_form.cleaned_data['usuario'],
		# 				login_form.cleaned_data['password'])
		# 		return redirect('/inicio/')
	#else:
	return render(request,'inicio.html')

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

def relacion_gastos(request):
	# if request.method == "POST":
	# 	form = RegistrarCondominioForm(request.POST)
	# 	if form.is_valid():
	# 		return redirect('/')
	# else:
	# 	formulario = RegistrarCondominioForm()
	# return render(request, 'condominio.html', 
	# 			{'formulario' : formulario,
	# 			'prueba': tuple(TipoEdificacion.objects.all())})
	return render(request, 'propietario/relacion_gastos.html')





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


	

class CostoServicioEspecialRegistrarView(CreateView):
	form_class = CostoServicioEspecialRegistrarForm
	template_name = 'administrador/registrar_costo_servicio_especial.html'
	success_url = reverse_lazy('administradora_app:costoServicioEspecialRegistrar')

	def form_valid(self, form):
		return super(CostoServicioEspecialRegistrarView, self).form_valid(form)


class CostoServicioMensualRegistrarView(CreateView):
	form_class = CostoServicioMensualRegistrarForm
	template_name ='administrador/registrar_costo_servicio_mensual.html'
	success_url = reverse_lazy('administradora_app:costoServicioMensualRegistrar')

	def form_valid(self, form):
		return super(CostoServicioMensualRegistrarView, self).form_valid(form)


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



class UsuarioRegistrarView(SuccessMessageMixin,CreateView):
	form_class = UsuarioRegistrarForm
	template_name = 'administrador/registrar_usuario.html'
	success_url = reverse_lazy('/')
	success_message = "Usuario pre-registrado con exito"
	#initial = {'condominio': 'defecto'}
	def form_valid(self, form):
		return super(UsuarioRegistrarView, self).form_valid(form)

class UsuarioListarView(ListView):
    template_name = 'administrador/listar_usuarios.html'
    model = Usuario

    def get_context_data(self, **kwargs):
        context = super(UsuarioListarView, self).get_context_data(**kwargs)
        return context



