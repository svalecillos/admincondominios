from django.conf.urls import patterns, url
from .views import *
from .views_servicios_especiales import *
from .views_servicios_mensuales import *
from .views_condominios import *
from .views_proveedores import *


urlpatterns = patterns('',

				url(r'^condominio/guiado$', 'apps.administradora.views.RegistrarCondominioGuiadoView', name='condominioRegistrarGuiado'),
				url(r'^administradora/registrar_edificacion/(?P<popup>\w{0,50})$', RegistrarTipoEdificacionView.as_view(), name='tipoEdificacionRegistrar'),	
				url(r'^registrar-usuario$',UsuarioRegistrarView.as_view(),name='usuarioRegistrar'),	
				url(r'^listar-usuario$',UsuarioListarView.as_view(),name='usuarioListar'),
				
				#url(r'^administradora/serviciomensual/registrar$', ServicioMensualRegistrarView.as_view(), name='servicioMensualRegistrar'),
				url(r'^administradora/costoservicioespecial/registrar$', CostoServicioEspecialRegistrarView.as_view(), name='costoServicioEspecialRegistrar'),
				url(r'^administradora/costoserviciomensual/registrar$', CostoServicioMensualRegistrarView.as_view(), name='costoServicioMensualRegistrar'),
				url(r'^registrar-pago$', 'apps.administradora.views.registrar_pago', name='registrar_pago'),
				url(r'^relacion-gastos$', 'apps.administradora.views.relacion_gastos', name='relacion_gastos'),
				url(r'^inicio/$', 'apps.administradora.views.inicio', name='inicio'),
				#condominios
				url(r'^condominio/$', CondominioListarView.as_view(), name='condominioListar'),
				url(r'^condominio/registrar$',CondominioRegistrarView.as_view(),name='condominioRegistrar'),						
				url(r'^condominio/detalle/(?P<pk>\d+)/$', CondominioDetalle.as_view(), name='condominioDetalle'),
				url(r'^condominio/actualizar/(?P<pk>\d+)/$', CondominioActualizar.as_view(), name='condominioActualizar'),
				url(r'^condominio/eliminar/(?P<pk>\d+)/$', CondominioEliminar.as_view(), name='condominioEliminar'),
				#proveedores
				url(r'^proveedor/$', ProveedorListarView.as_view(), name='proveedorListar'),
				url(r'^proveedor/registrar$', ProveedorRegistrarView.as_view(), name='proveedorRegistrar'),						
				url(r'^proveedor/detalle/(?P<pk>\d+)/$', ProveedorDetalle.as_view(), name='proveedorDetalle'),
				url(r'^proveedor/actualizar/(?P<pk>\d+)/$', ProveedorActualizar.as_view(), name='proveedorActualizar'),
				url(r'^proveedor/eliminar/(?P<pk>\d+)/$', ProveedorEliminar.as_view(), name='proveedorEliminar'),				
				#servicios mensuales
				url(r'^servicioMensual/$', ServicioMensualListarView.as_view(), name='servicioMensualListar'),
				url(r'^servicioMensual/registrar$', ServicioMensualRegistrarView.as_view(), name='servicioMensualRegistrar'),						
				url(r'^servicioMensual/detalle/(?P<pk>\d+)/$', ServicioMensualDetalle.as_view(), name='servicioMensualDetalle'),
				url(r'^servicioMensual/actualizar/(?P<pk>\d+)/$', ServicioMensualActualizar.as_view(), name='servicioMensualActualizar'),
				url(r'^servicioMensual/eliminar/(?P<pk>\d+)/$',ServicioMensualEliminar, name='servicioMensualEliminar'),
				#servicios esepciales
				url(r'^servicioEspecial/$', ServicioEspecialListarView.as_view(), name='servicioEspecialListar'),
				url(r'^servicioEspecial/registrar$', ServicioEspecialRegistrarView.as_view(), name='servicioEspecialRegistrar'),
				url(r'^servicioEspecial/detalle/(?P<pk>\d+)/$', ServicioEspecialDetalle.as_view(), name='servicioEspecialDetalle'),
				url(r'^servicioEspecial/actualizar/(?P<pk>\d+)/$', ServicioEspecialActualizar.as_view(), name='servicioEspecialActualizar'),
				url(r'^servicioEspecial/eliminar/(?P<pk>\d+)/$',ServicioEspecialEliminar, name='servicioEspecialEliminar'),
	)