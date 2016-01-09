from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrarUsuarioForm, LoginForm
from apps.administradora.forms import *
from apps.administradora.models import *
from .models import Usuario
from .functions import LogIn


@login_required()
def inicio(request):
	return render(request, 'inicio.html')

def login(request):
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
				LogIn(request, login_form.cleaned_data['usuario'],
						login_form.cleaned_data['password'])
				return redirect('/inicio/')
	else:
		login_form = LoginForm()
	return render(request, 'usuario/login.html', 
				{'login_form' : login_form})

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
			 	password = registrar_usuario.cleaned_data['password'])
			# LogIn(request, registrar_usuario.cleaned_data['usuario'],
			# 		registrar_usuario.cleaned_data['password'])
			# print (registrar_usuario.cleaned_data['usuario'])
			return redirect('/')
	else:
		registrar_usuario = RegistrarUsuarioForm()
	return render(request, 'usuario/registro.html', 
				{'registrar_usuario' : registrar_usuario})

#def condominio(request):
#	return render(request, 'index.html')

@login_required()
def logOut(request):
	logout(request)
	return redirect('/')










