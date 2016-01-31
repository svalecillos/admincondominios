from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from apps.usuarios.models import Usuario
from .models import *
from .forms import *
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse

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

class ServicioEspecialRegistrarView(CreateView):

	form_class = RegistrarServicioEspecialForm
	template_name = 'administrador/registrar_servicio_especial.html'
	success_url = reverse_lazy('administradora_app:servicioEspecialRegistrar')

	def form_valid(self, form):
		print("\n")
		print("\n--------------------------------------------------\n")
		print(self.request.POST)
		return super(ServicioEspecialRegistrarView, self).form_valid(form)		

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









class CondominioRegistrarView(SuccessMessageMixin,CreateView):

	form_class = RegistrarCondominioForm
	template_name = 'administrador/registrar_condominio.html'
	success_url = reverse_lazy('administradora_app:condominioRegistrar')
	success_message = "Condominio creado con exito"

	def form_valid(self, form):
		form.instance.creadoPor = Usuario.objects.get(pk=self.request.user.id)
		return super(CondominioRegistrarView, self).form_valid(form)

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

class CondominioEliminar(SuccessMessageMixin,DeleteView):

    template_name = 'administrador/eliminar_condominio.html'
    model = Condominio
    success_message = "Condominio eliminado con exito"
    success_url = '/condominio'



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






class ServicioMensualRegistrarView(SuccessMessageMixin,CreateView):

	form_class = RegistrarServicioMensualForm
	template_name = 'administrador/registrar_servicio_mensual.html'
	success_url = reverse_lazy('administradora_app:servicioMensualRegistrar')
	success_message='Servicio asociado exitosamente'

	def form_valid(self, form):
		return super(ServicioMensualRegistrarView, self).form_valid(form)

class ServicioMensualListarView(ListView):

    template_name = 'administrador/listar_servicio_mensual.html'
    #model = ServicioMensual
    queryset = ServicioMensual.objects.filter(estatus=1) #donde el servico este activo

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
	if request.method == "POST":
		if request.POST:
			obj=ServicioMensual.objects.get(pk=pk)
			obj.estatus=0
			obj.save()
			return redirect('/servicioMensual')
	else:
		return render(request, 'administrador/eliminar_servicio_mensual.html', 
				{'ServicioMensual' : ServicioMensual.objects.get(pk=pk)})    
