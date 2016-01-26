from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
	url(r'^',include('apps.usuarios.urls', namespace="usuarios_app")),
	url(r'^',include('apps.administradora.urls', namespace="administradora_app")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('apps.api.urls')),
]
