from distutils.text_file import TextFile
from pyexpat import model
from django.db import models

# Create your models here.
class Hortelano(models.Model):
    nombre = models.CharField(max_length=80)
    apodo = models.CharField(max_length=30)
    mail = models.EmailField(max_length=254, blank=True )
    def __str__(self):
        return self.nombre +' '+ self.apodo


class Huerta(models.Model):
    hortelano = models.ForeignKey(Hortelano,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    coord_x = models.FloatField(blank=True)
    coord_y = models.FloatField(blank=True)
    ancho = models.SmallIntegerField(blank=True)
    largo = models.SmallIntegerField(blank=True)
    def __str__(self):
        return self.nombre


class Canteros(models.Model):
    huerta = models.ForeignKey(Huerta,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    ancho = models.SmallIntegerField()
    largo = models.SmallIntegerField()
    
    def __str__(self):
        return self.nombre
