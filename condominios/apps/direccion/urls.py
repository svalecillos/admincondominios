from django.conf.urls import patterns, url

urlpatterns = patterns('apps.direccion.views',
						url(r'^$', 'index', name="index"),
	)
	
