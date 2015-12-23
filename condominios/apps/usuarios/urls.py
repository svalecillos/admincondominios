from django.conf.urls import patterns, url

urlpatterns = patterns('',
						url(r'^login/$', 'apps.usuarios.views.inicio', name="login"),
						url(r'^login/home/$', 'apps.usuarios.views.index', name='index'),
						url(r'^registro/$', 'apps.usuarios.views.registro', name="registro"),
						url(r'^salir/$', 'apps.usuarios.views.logOut', name="logOut")						
	)
	