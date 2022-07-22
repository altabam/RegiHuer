from distutils.text_file import TextFile
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Hortelano(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE )
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
    ubicacion_x = models.SmallIntegerField()
    ubicacion_y = models.SmallIntegerField()
    
    def __str__(self):
        return self.nombre



class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    web = models.URLField(blank=True)

    # Python 3
    def __str__(self): 
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()