from django.db import models
from configuracion.models import Hortelano, Cultivos
# Create your models here.
class Huerta(models.Model):
    hortelano = models.ForeignKey(Hortelano,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    coord_x = models.FloatField(blank=True)
    coord_y = models.FloatField(blank=True)
    ancho = models.FloatField(blank=True)
    largo = models.FloatField(blank=True)
    def __str__(self):
        return self.nombre  


class Canteros(models.Model):
    huerta = models.ForeignKey(Huerta,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    ancho = models.FloatField(blank=True)
    largo = models.FloatField(blank=True)
    ubicacion_x = models.FloatField(blank=True)
    ubicacion_y = models.FloatField(blank=True)
    
    def __str__(self):
        return self.nombre +" "+ self.huerta.nombre

class Cantero_Cultivos(models.Model):
    cantero = models.ForeignKey(Canteros,on_delete=models.CASCADE)
    cultivo = models.ForeignKey(Cultivos,on_delete=models.CASCADE)
    fechaSiembra = models.DateField(blank=True, null=True)
    fechaCosecha = models.DateField(blank=True, null=True)
    cantidad_sembrada = models.SmallIntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.cantero.nombre +"-"+ self.cultivo.nombre



