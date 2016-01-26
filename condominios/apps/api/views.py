import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

def ApiPrueba(request):
	#if request.method == "GET":
	response_data = {}
	response_data['id'] = 'failed'
	response_data['literal'] = 'You messed up'
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def select(request):
	return render(request, 'api/ajax_prueba.html')