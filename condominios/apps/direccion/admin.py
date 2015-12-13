from django.contrib import admin
from .models import *
from apps.venezuela.models import *


admin.site.register(Estados)

class MunicipiosAdmin(admin.ModelAdmin):
    list_display = ('municipio', 'estado',)
    list_filter = (('estado', admin.RelatedOnlyFieldListFilter),)
admin.site.register(Municipios, MunicipiosAdmin)


#admin.site.register(Municipios)
admin.site.register(Parroquias)

admin.site.register(Estado)
admin.site.register(Ciudad)
admin.site.register(Parroquia)
admin.site.register(Municipio)