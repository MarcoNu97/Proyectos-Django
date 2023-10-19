from django.db import models
from aplications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.
class Habilidades (models.Model):
    Habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
        ordering = ['Habilidad']
        unique_together = ('Habilidad',)

    def __str__(self):
        return self.Habilidad
    

class Empleado (models.Model):

    JOB_OPCIONES=(
        ('0', 'Contador'),
        ('1', 'Administrativo'),
        ('2', 'Desarrollador'),
        ('3', 'Otro'),
 
    )

    nombre = models.CharField('Nombre', max_length=60)
    apellido = models.CharField('Apellido', max_length=60)
    trabajo = models.CharField('Puesto', max_length=1, choices=JOB_OPCIONES)
    Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    observaciones = RichTextField(default="")
    Habilidades = models.ManyToManyField(Habilidades)
    
    def __str__(self):
        return self.nombre + '-' + self.apellido + '-' + self.trabajo 
        