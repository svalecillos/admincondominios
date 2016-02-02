from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
				url(r'^ajax/prueba$', 'apps.api.views.ApiPrueba', name='ajaxPrueba'),
				url(r'^ajax/estados$', 'apps.api.views.estados', name='ajaxEstados'),
				url(r'^ajax/municipios$', 'apps.api.views.municipios', name='ajaxmunicipios'),
				url(r'^ajax/parroquias$', 'apps.api.views.parroquias', name='ajaxparroquias'),
				url(r'^ajax/condominios$', 'apps.api.views.condominios', name='ajaxcondominios'),
				url(r'^ajax/proveedores$', 'apps.api.views.proveedores', name='ajaxproveedores'),
				url(r'^ajax/select$', 'apps.api.views.select', name='select'),
				url(r'^ajax/select_estados$', 'apps.api.views.select_estados', name='select_estados'),
				url(r'^ajax/buscar_condominio$', 'apps.api.views.buscar_condominios', name='buscar_condominios'),
	)
