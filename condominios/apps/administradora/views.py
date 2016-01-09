from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .models import *
from apps.usuarios.models import Usuario
from .forms import *
from django.core.urlresolvers import reverse, reverse_lazy


def index(request):
	
	formulario_contacto = Contact_form()
	return render(request,'index.html',{'Contact_form' : formulario_contacto})

def envio_correo(request):
	if request.is_ajax():
		asunto = 'Nuevo mensaje desde la pagina web Administradora JJ24-30'
		mensaje = """%s | %s

%s"""%(request.POST['inputName'], request.POST['inputEmail'], request.POST['inputMensaje'])
		remitente = 'correo@gmail.com'
		destinatario = ['correo@gmail.com']
		mail = EmailMessage(asunto, mensaje, remitente, destinatario)
		mail.send(fail_silently=False)
		return HttpResponse(' ')

	else:
		return redirect('/')

class CondominioRegistrarView(CreateView):

	form_class = RegistrarCondominioForm
	template_name = 'condominio/registrar.html'
	success_url = reverse_lazy('administradora_app:condominioRegistrar')

	def form_valid(self, form):
		form.instance.creadoPor = Usuario.objects.get(pk=1)
		return super(CondominioRegistrarView, self).form_valid(form)

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
		form.instance.creadoPor = Usuario.objects.get(pk=1)
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


class CondominioListarView(DetailView):

    template_name = 'condominio/listar.html'
    #model = Condominio
    def get_queryset(self):
        return super(Condominio, self).objects.all()

    def get_context_data(self, **kwargs):
        context = super(CondominioListarView, self).get_context_data(**kwargs)
        context['condominios'] = Condominio.objects.all()
        return context    