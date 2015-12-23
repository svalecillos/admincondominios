from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
				url(r'^$', 'apps.administradora.views.index', name="index"),
				url(r'^envio_correo/$', 'apps.administradora.views.envio_correo', name="envio_correo"),
				url(r'^administradora/condominio/registrar$',CondominioRegistrarView.as_view(),name='condominioRegistrar'),						
				url(r'^administradora/proveedor/registrar$', ProveedorRegistrarView.as_view(), name='proveedorRegistrar'),
				url(r'^administradora/servicioespecial/registrar$', ServicioEspecialRegistrarView.as_view(), name='servicioEspecialRegistrar'),
				url(r'^administradora/serviciomensual/registrar$', ServicioMensualRegistrarView.as_view(), name='servicioMensualRegistrar'),
				url(r'^administradora/costoservicioespecial/registrar$', CostoServicioEspecialRegistrarView.as_view(), name='costoServicioEspecialRegistrar'),
				url(r'^administradora/costoserviciomensual/registrar$', CostoServicioMensualRegistrarView.as_view(), name='costoServicioMensualRegistrar'),
				#url(r'^administradora/condominio/listar$', CondominioListarView.as_view(), name='condominioListar'),
				#url(r'^salir/$', 'apps.usuarios.views.logOut', name="logOut")						
	)
	