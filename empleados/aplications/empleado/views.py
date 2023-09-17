from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

class PruebaLista (ListView):
    template_name = 'empleado/Lista.html'
    queryset = ['A', 'B', 'C']
    context_object_name = 'Lista_Prueba'