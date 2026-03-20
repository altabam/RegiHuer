from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
MES = (
        ('ENE', 'Enero'),
        ('FEB', 'Febrero'),
        ('MAR', 'Marzo'),
        ('ABR', 'Abril'),
        ('MAY', 'Mayo'),
        ('JUN', 'Junio'),
        ('JUL', 'Julio'),
        ('AGO', 'Agosto'),
        ('SEP', 'Septiembre'),
        ('OCT', 'Octubre'),
        ('NOV', 'Noviembre'),
        ('DIC', 'Diciembre'),
    )

SEMANA = (
        ('1', 'Primer Semana'),
        ('2', 'Segunda Semana'),
        ('3', 'Tercer Semana'),
        ('4', 'Cuarta Semana'),
    )

class Hortelano(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE )
    apodo = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return self.usuario.first_name+" "+self.usuario.last_name +' '+ self.apodo


class Suelos(models.Model):
    desc_corta = models.CharField(max_length=30, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.desc_corta

class Riego_Cultivo(models.Model):
    desc_corta = models.CharField(max_length=30, blank=True)
    cantidad = models.SmallIntegerField()
    frecuencia = models.SmallIntegerField()
    descripcion = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.desc_corta + "cant por vez: " + str(self.cantidad) + "frecuencia dias: " +str(self.frecuencia) 

class Plagas(models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)
    tratamiento = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.nombre

class Enfermedades(models.Model):
    AGENTE_CAUSAL = (
        ('HON', 'Hongos'),
        ('BAC', 'Bacterias'),
        ('NEM', 'Nematodos'),
        ('VIR', 'Virus'),
        ('PAR', 'Plantas Parasitas'),
    )
    nombre = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)
    tratamiento = models.CharField(max_length=255, blank=True)
    agente_causal = models.CharField(max_length=3, choices=AGENTE_CAUSAL)
    sintomas = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    web = models.URLField(blank=True)

    # Python 3
    def __str__(self): 
        return self.usuario.username



 
class Cultivos(models.Model):
    TIPOS_SIEMBRA = (
        ('D', 'Directa'),
        ('S', 'Semillero'),
        ('T', 'Directa / Semillero'),
    )
    LUNA =(
        ('C','Cuarto Creciente'),
        ('M','Cuarto Menguante'),
        ('L','Llena'),
        ('N','Nueva'),
    )
    FAMILIA =(
        ('COM','Compuestas'),
        ('CRU','Cruciferas (Brásicas)'),
        ('UMB','Cruciferas'),
        ('SOL','Solanaceas'),
        ('GRA','Gramineas'),
        ('LEG','Leguminosas'),
        ('QUE','Quenopoidaceas'),
        ('ALL','Alliaceas'),
        ('CUC','Cucurbitaceas'),
        ('CON','Convolvulaceas'),
        ('ASP','Asparagaceae'),
        ('API','Apiaceae'),
    )
    familia = models.CharField(max_length=3, choices=FAMILIA)
    nombre_cientifico = models.CharField(max_length=50, blank=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    tipo_siembra = models.CharField(max_length=1, choices=TIPOS_SIEMBRA)
    luna_siembra = models.CharField(max_length=1, choices=LUNA, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.familia})"





class Fecha_Siembra(models.Model):
    semana= models.CharField(max_length=1, choices=SEMANA, null=True)
    mes= models.CharField(max_length=3, choices=MES, null=True)
    def __str__(self):
        return f"{self.cultivo.mes} - {self.semana}"

    

class Variedades_Cultivos(models.Model):
    nombre = models.CharField(max_length=50)
    cultivo = models.ForeignKey(Cultivos,on_delete=models.CASCADE, related_name="variedades")
    imagen = models.ImageField(upload_to='cultivos',blank=True, null=True)
    descripcion = models.TextField(blank=True)
    class Meta:
        ordering = ["nombre"]
    
    def __str__(self):
        return f"{self.cultivo.nombre} - {self.nombre}"

class Luz_Variedades_Cultivos(models.Model):
    variedad_cultivo = models.ForeignKey(Variedades_Cultivos,on_delete=models.CASCADE,related_name="luz")
    desc_corta = models.CharField(max_length=30, blank=True)
    valor_minimo = models.IntegerField( blank=True, null=True)
    valor_maximo = models.IntegerField( blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return f"{self.variedad_cultivo.nombre} - {self.desc_corta} / {self.valor_minimo} - {self.valor_maximo}"


class Temperaturas_Variedades_Cultivos(models.Model):
    variedad_cultivo = models.ForeignKey(Variedades_Cultivos,on_delete=models.CASCADE,related_name="temperatura")
    desc_corta = models.CharField(max_length=30, blank=True)
    valor_minimo = models.IntegerField( blank=True, null=True)
    valor_maximo = models.IntegerField( blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.variedad_cultivo.nombre + self.desc_corta + str(self.valor_minimo) +"-"+ str(self.valor_maximo)



class Fecha_Siembra_Variedades_Cultivos(models.Model):
    variedad_cultivo = models.ForeignKey(Variedades_Cultivos,on_delete=models.CASCADE, null=True, blank=True, related_name="fecha_siembra")
    fecha_siembra_desde = models.ForeignKey(Fecha_Siembra,on_delete=models.CASCADE, null=True, blank=True, related_name="fecha_siembra_desde")
    fecha_siembra_hasta = models.ForeignKey(Fecha_Siembra,on_delete=models.CASCADE, null=True, blank=True, related_name="fecha_siembra_hasta")
    def __str__(self):
        return f"Desde: {self.fecha_siembra_desde} hasta: {self.fecha_siembra_hasta}"

class Tiempos_Variedades_Cultivos(models.Model):
    TIPO = (
        ('G', 'Germinacion'),
        ('T', 'Trasplante'),
        ('C', 'Cosecha'),
    )
    CONDICIONES = (
        ('O', 'Optimo'),
        ('N', 'Normal'),
        ('M', 'Como maximo'),
    )
    variedad_cultivo = models.ForeignKey(Variedades_Cultivos,on_delete=models.CASCADE, null=True, blank=True)
    condicion =  models.CharField(max_length=1, choices=CONDICIONES)
    dia_desde = models.SmallIntegerField(blank=0)
    dia_hasta = models.SmallIntegerField(blank=0)
    observacion = models.CharField(max_length=50, blank=True)
    
class Suelos_Cultivos(models.Model):
    cultivo = models.ForeignKey(Cultivos,on_delete=models.CASCADE, null=True, blank=True)
    suelo = models.ForeignKey(Suelos,on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.cultivo.nombre + "var:" + self.nombre
class Asociaciones_Cultivos(models.Model):
    cultivo = models.ForeignKey(Cultivos,on_delete=models.CASCADE, null=True, blank=True)
    asociacion = models.ForeignKey(Cultivos,on_delete=models.CASCADE, null=True, blank=True,related_name='%(class)s_asociacion')
    beneficiosa = models.BooleanField(max_length=255, blank=True)

class Plagas_Cultivos(models.Model):
    cultivo = models.ForeignKey(Cultivos,on_delete=models.CASCADE, null=True, blank=True)
    plagas =   models.ForeignKey(Plagas,on_delete=models.CASCADE,  null=True, blank=True)

class Enfermedades_Cultivos(models.Model):
    cultivo = models.ForeignKey(Cultivos,on_delete=models.CASCADE, null=True, blank=True)
    enfermedades  = models.ForeignKey(Enfermedades,on_delete=models.CASCADE, null=True, blank=True)

class Galeria(models.Model):
    nombre = models.CharField(max_length=60)
    

class GaleriaImagen(models.Model):
    nombre = models.CharField(max_length=60)
    imagen = models.ImageField(upload_to='galeriaPrincipal',blank=True)
    leyenda = models.CharField(max_length=255,blank=True)
    galeria = models.ForeignKey(Galeria,on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()