from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
				url(r'^registrar-usuario$',UsuarioRegistrarView.as_view(),name='usuarioRegistrar'),	
				url(r'^listar-usuario$',UsuarioListarView.as_view(),name='usuarioListar'),	
				url(r'^condominio/registrar$',CondominioRegistrarView.as_view(),name='condominioRegistrar'),	
				url(r'^administradora/proveedor/registrar$', ProveedorRegistrarView.as_view(), name='proveedorRegistrar'),
				url(r'^administradora/servicioespecial/registrar$', ServicioEspecialRegistrarView.as_view(), name='servicioEspecialRegistrar'),
				url(r'^administradora/serviciomensual/registrar$', ServicioMensualRegistrarView.as_view(), name='servicioMensualRegistrar'),
				url(r'^administradora/costoservicioespecial/registrar$', CostoServicioEspecialRegistrarView.as_view(), name='costoServicioEspecialRegistrar'),
				url(r'^administradora/costoserviciomensual/registrar$', CostoServicioMensualRegistrarView.as_view(), name='costoServicioMensualRegistrar'),
				url(r'^registrar-pago$', 'apps.administradora.views.registrar_pago', name='registrar_pago'),
				url(r'^historial-movimientos$', 'apps.administradora.views.historial_movimientos', name='historial_movimientos'),
				url(r'^condominio/$', CondominioListarView.as_view(), name='condominioListar'),						
				url(r'^condominio/detalle/(?P<pk>\d+)/$', CondominioDetailView.as_view(), name='condominioDetalle'),
				url(r'^condominio/actualizar/(?P<pk>\d+)/$', CondominioUpdate.as_view(), name='condominioActualizar'),
				#url(r'^condominio/guiado$', RegistrarCondominioGuiadoView.as_view(), name='condominioRegistrarGuiado'),
				url(r'^administradora/registrar_edificacion/(?P<popup>\w{0,50})$', RegistrarTipoEdificacionView.as_view(), name='tipoEdificacionRegistrar'),
				url(r'^condominio/guiado$', 'apps.administradora.views.RegistrarCondominioGuiadoView', name='condominioRegistrarGuiado'),
				
	)
