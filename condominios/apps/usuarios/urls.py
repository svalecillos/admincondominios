from django.conf.urls import patterns, url

urlpatterns = patterns('',
						url(r'^$', 'apps.usuarios.views.index', name="index"),
						url(r'^envio-correo/$', 'apps.usuarios.views.envio_correo', name="envio_correo"),
						url(r'^registro/$', 'apps.usuarios.views.registro', name="registro"),
						url(r'^salir/$', 'apps.usuarios.views.logOut', name="logOut")						
	)
	