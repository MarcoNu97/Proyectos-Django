from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('list_cursos/', views.list_cursos, name='list_cursos'),
    # path('registrarCurso/', views.registrarCurso),
    # path('edicionCurso/<codigo>', views.edicionCurso),
    # path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
]