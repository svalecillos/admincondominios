from django.conf.urls import patterns, url

urlpatterns = patterns('',
				url(r'^$', 'apps.administradora.views.index', name="index"),

				#url(r'^salir/$', 'apps.usuarios.views.logOut', name="logOut")						
	)
	