from django.contrib import admin
from .models import *


admin.site.register(Estado)
admin.site.register(Ciudad)
admin.site.register(Municipio)
admin.site.register(PrefijoTelefonico)
admin.site.register(prefijoCelular)

class ParroquiasAdmin(admin.ModelAdmin):
    list_display = ('parroquia', 'municipio',)
    list_filter = (('municipio', admin.RelatedOnlyFieldListFilter),)
admin.site.register(Parroquia, ParroquiasAdmin)
