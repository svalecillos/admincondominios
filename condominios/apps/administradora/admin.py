from django.contrib import admin
from .models import *

admin.site.register(Condominio)
admin.site.register(Proveedor)
admin.site.register(TipoEdificacion)
admin.site.register(ServicioMensual)
admin.site.register(ServicioEspecial)

class CostoServicioMensualAdmin(admin.ModelAdmin):
    list_display = ('servicioMensual', 'costo',)
admin.site.register(CostoServicioMensual,CostoServicioMensualAdmin)

class CostoServicioEspecialAdmin(admin.ModelAdmin):
    list_display = ('servicioEspecial', 'costo',)
admin.site.register(CostoServicioEspecial,CostoServicioEspecialAdmin)

admin.site.register(CargoServicioMensual)
admin.site.register(CargoServicioEspecial)

class CuentaUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'saldo',)
    #list_filter = (('municipio', admin.RelatedOnlyFieldListFilter),)
admin.site.register(CuentaUsuario,CuentaUsuarioAdmin)


admin.site.register(CuentaCondominio)
admin.site.register(Transaccion)

