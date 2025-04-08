from django.contrib import admin
from .models import Hortelano,  Galeria, GaleriaImagen, Cultivos

# Register your models here.
admin.site.register(Hortelano)
admin.site.register(Galeria)
admin.site.register(GaleriaImagen)
admin.site.register(Cultivos)

