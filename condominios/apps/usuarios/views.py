from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import *
from .forms import *
from .models import Usuario
from .functions import *

def index(request):
	if request.method == "POST":
		# if 'register_form' in request.POST:
		# 	registrar_usuario = RegistrarUsuarioForm(request.POST)
		# 	if registrar_usuario.is_valid():
		# 		Usuario.objects.create_user(usuario = registrar_usuario.cleaned_data['usuario'],
		# 		 correo = registrar_usuario.cleaned_data['correo'], 
		# 		 password = registrar_usuario.cleaned_data['password'])
		# 		LogIn(request, registrar_usuario.cleaned_data['usuario'],
		# 				registrar_usuario.cleaned_data['password'])
		# 		return redirect('/')
		# if 'login_form' in request.POST:
			login_form = LoginForm(request.POST)
			if login_form.is_valid():
				LogIn(request, login_form.cleaned_data['usuario'],login_form.cleaned_data['password'])
				return redirect('/inicio/')
	else:
		formulario_contacto = Contact_form()
		login_form = LoginForm()
	return render(request,'index.html',{'Contact_form' : formulario_contacto,'login_form' : login_form})
	
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

def registro(request):
	if request.method == "POST":
		registrar_usuario = RegistrarUsuarioForm(request.POST)
		if registrar_usuario.is_valid():
			Usuario.objects.create_user(
				usuario = registrar_usuario.cleaned_data['usuario'],
				cedula = registrar_usuario.cleaned_data['cedula'],
				nombre = registrar_usuario.cleaned_data['nombre'],
				apellido = registrar_usuario.cleaned_data['apellido'],
			 	correo = registrar_usuario.cleaned_data['correo'],
			 	rol = registrar_usuario.cleaned_data['rol'],
			 	password = registrar_usuario.cleaned_data['password'])
			# LogIn(request, registrar_usuario.cleaned_data['usuario'],
			# 		registrar_usuario.cleaned_data['password'])
			# print (registrar_usuario.cleaned_data['usuario'])
			return redirect('/')
	else:
		registrar_usuario = RegistrarUsuarioForm()
	return render(request, 'usuario/registro.html', 
				{'registrar_usuario' : registrar_usuario})

@login_required()
def logOut(request):
	logout(request)
	return redirect('/')