from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UsuarioPromesa(  models.Model):
    first_name = models.CharField( max_length=150)
    last_name = models.CharField( max_length=150)
    username = models.CharField(max_length=80, unique=True)
    email = models.EmailField(unique=True)
    fecha = models.DateTimeField(auto_now_add=True)
    aleatorio = models.CharField(max_length=60)
    token = models.TextField()
    def __str__(self):
        return self.first_name + self.last_name + self.username
