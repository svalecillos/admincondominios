from django.conf.urls import patterns, url

urlpatterns = patterns('',
				url(r'^geo/(?P<type>estados)/$', 'apps.venezuela.views.geo', name='geo'),
				url(r'^geo/(?P<type>ciudades|municipios|parroquias)/(?P<parent_id>[0-9]+)$', 'apps.venezuela.views.geo', name='geo'),				
	)
	