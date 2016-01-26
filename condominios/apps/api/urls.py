from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
				url(r'^ajax/prueba$', 'apps.api.views.ApiPrueba', name='ajaxPrueba'),
				url(r'^ajax/select$', 'apps.api.views.select', name='select'),
	)
