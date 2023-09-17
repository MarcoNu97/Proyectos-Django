from django.contrib import admin
from .models import Departamento

# # Register your models here.
class DepartamentoAdmin (admin.ModelAdmin):
    list_display = (
        'nombre',
        'sigla',
        'activo',
        'piso',

    )
    
admin.site.register(Departamento, DepartamentoAdmin)