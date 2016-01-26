import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from apps.administradora.models import Condominio
from apps.venezuela.models import *

def ApiPrueba(request):

	response_data = {}
	response_data['id'] =  list(Condominio.objects.values('condominio'))
	#response_data['id'] =  list(Condominio.objects.values_list('condominio'))
	response_data['literal'] = ['A','B','L','L','L','L','L','L']
	if request.is_ajax():
		return JsonResponse(response_data)
	else:
		return JsonResponse(response_data)
		#return HttpResponse(json.dumps(response_data), content_type="application/json")


def estados(request):

	response_data = {}
	#response_data['id'] =  list(Estado.objects.values('id'))
	#response_data['estado'] = list(Estado.objects.values('estado'))
	response_data['resultado'] =  list(Estado.objects.values('id','estado'))
	if request.is_ajax():
		return JsonResponse(response_data)
	else:
		return JsonResponse(response_data)

def municipios(request):

	if request.is_ajax():
		response_data = {}
		response_data['resultado'] =  list(Municipio.objects.values('id','municipio').filter(estado_id=request.POST['elegido']))		
		return JsonResponse(response_data)
	else:
		response_data = {}
		response_data['resultado'] =  list(Municipio.objects.values('id','municipio').filter(estado_id=request.GET['elegido']))
		return JsonResponse(response_data)

def parroquias(request):

	if request.is_ajax():
		response_data = {}
		response_data['resultado'] =  list(Parroquia.objects.values('id','parroquia').filter(municipio_id=request.POST['elegido']))		
		return JsonResponse(response_data)
	else:
		response_data = {}
		response_data['resultado'] =  list(Parroquia.objects.values('id','parroquia').filter(municipio_id=request.GET['elegido']))
		return JsonResponse(response_data)

def select(request):
	return render(request, 'api/ajax_prueba.html')

def select_estados(request):
	return render(request, 'api/ajax_select_estados.html')