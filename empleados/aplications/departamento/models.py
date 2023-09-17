from django.db import models

# Create your models here.

class Departamento (models.Model):
    
    nombre = models.CharField('Nombre', max_length=50, blank=True)
    sigla = models.CharField('Sigla', max_length=30)
    activo = models.BooleanField('¿Esta activo?', default=False)
    piso = models.CharField('Piso', max_length=5, blank=True)
    oficina = models.CharField('Oficina N*', max_length=10, blank=True)

    def __str__(self):
        return self.nombre + '-' + self.sigla + '-' + self.piso + '-' + self.oficina
    
    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'
        ordering = ['nombre']
        unique_together = ('nombre', 'sigla',)