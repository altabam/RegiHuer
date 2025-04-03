from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Group

# Create your models here.
class Menu(models.Model):
    TIPO = (
        ('P', 'Padre'),
        ('I', 'Intermedio'),
        ('H', 'Hoja'),
    )
    url = models.CharField(max_length=250, blank=True,null=True)
    nombre = models.CharField(max_length=250,unique=True)
    tipo = models.CharField(max_length=1, choices=TIPO)
    menuPadre = models.ForeignKey("self",related_name="subMenu",on_delete=models.CASCADE,blank=True,null=True, )

    # no es el mejor modo de retornar la URL pero es facil de entender :D
    def get_absolute_url(self):
        return "%s" % self.url 
        
    def __unicode__(self):
        return u'%s' % self.nombre

    def __str__(self):
      return f"{self.url} {self.nombre} {self.tipo}"
    

class MenuGroup(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    def __str__(self):
      return f"{self.menu} {self.groups}"
    
    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('author-detail', args=[str(self.id)])


