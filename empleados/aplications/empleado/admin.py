from django.contrib import admin
from django.http import HttpResponse
from django.db import models
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Empleado, Habilidades
from ckeditor.widgets import CKEditorWidget

# Register your models here.
admin.site.register(Habilidades)

# Función de exportación a CSV
#--#
def export_selected_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Empleados.csv"'
    writer = csv.writer(response)
    writer.writerow(['nombre', 'apellido', 'trabajo', 'Departamento']) 

# Encabezados
#--#
    for Empleado in queryset:
        writer.writerow([Empleado.nombre, Empleado.apellido, Empleado.trabajo, Empleado.Departamento])

    return response

export_selected_to_csv.short_description = "Exportar seleccionados a CSV"

# Función de exportación a PDF
#--#
def export_selected_to_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Empleados.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, "Listado de Empleados")
    p.drawString(100, 730, "---------------------------------------------")

    y = 700
    for Empleado in queryset:
        p.drawString(100, y, f"nombre: {Empleado.nombre}")
        p.drawString(205, y, f"apellido: {Empleado.apellido}")
        p.drawString(300, y, f"trabajo: {Empleado.trabajo}")
        p.drawString(375, y, f"Departamento: {Empleado.Departamento}")
        y -= 45

    p.showPage()
    p.save()

    return response


class EmpleadoAdmin (admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'trabajo',
        'Departamento',

    )

    search_fields = (
        'apellido',
        'nombre',
    )
    
    actions = [export_selected_to_csv, export_selected_to_pdf]

admin.site.register(Empleado, EmpleadoAdmin)

formfield_overrides = {
    models.TextField: {'widget': CKEditorWidget()},

   }