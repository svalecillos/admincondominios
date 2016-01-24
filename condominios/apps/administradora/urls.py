from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
				url(r'^administradora/condominio/registrar$',CondominioRegistrarView.as_view(),name='condominioRegistrar'),	
				url(r'^administradora/proveedor/registrar$', ProveedorRegistrarView.as_view(), name='proveedorRegistrar'),
				url(r'^administradora/servicioespecial/registrar$', ServicioEspecialRegistrarView.as_view(), name='servicioEspecialRegistrar'),
				url(r'^administradora/serviciomensual/registrar$', ServicioMensualRegistrarView.as_view(), name='servicioMensualRegistrar'),
				url(r'^administradora/costoservicioespecial/registrar$', CostoServicioEspecialRegistrarView.as_view(), name='costoServicioEspecialRegistrar'),
				url(r'^administradora/costoserviciomensual/registrar$', CostoServicioMensualRegistrarView.as_view(), name='costoServicioMensualRegistrar'),
				url(r'^registrar-pago$', 'apps.administradora.views.registrar_pago', name='registrar_pago'),
				url(r'^historial-movimientos$', 'apps.administradora.views.historial_movimientos', name='historial_movimientos'),
				url(r'^condominio-listar$', CondominioListarView.as_view(), name='condominioListar'),						
				url(r'^condominio/(?P<pk>\d+)/$', CondominioDetailView.as_view(), name='condominioDetalle'),
				#url(r'^condominio/guiado$', RegistrarCondominioGuiadoView.as_view(), name='condominioRegistrarGuiado'),
				url(r'^administradora/registrar_edificacion/(?P<popup>\w{0,50})$', RegistrarTipoEdificacionView.as_view(), name='tipoEdificacionRegistrar'),
				url(r'^condominio/guiado$', 'apps.administradora.views.RegistrarCondominioGuiadoView', name='condominioRegistrarGuiado'),
				
	)
