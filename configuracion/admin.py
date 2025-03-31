from django.contrib import admin
from .models import Hortelano, Huerta, Galeria, GaleriaImagen

# Register your models here.
admin.site.register(Hortelano)
admin.site.register(Huerta)
admin.site.register(Galeria)
admin.site.register(GaleriaImagen)

