from django.conf.urls import patterns, url

urlpatterns = patterns('',
						url(r'^login/$', 'apps.usuarios.views.login', name="login"),
						url(r'^inicio/$', 'apps.usuarios.views.inicio', name='inicio'),
						url(r'^registro/$', 'apps.usuarios.views.registro', name="registro"),
						url(r'^salir/$', 'apps.usuarios.views.logOut', name="logOut")						
	)
	