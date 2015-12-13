from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def LogIn(request, usuario, password):
	usuario = authenticate(usuario = usuario, password = password)
	if usuario is not None:
		if usuario.is_active:
			login(request, usuario)