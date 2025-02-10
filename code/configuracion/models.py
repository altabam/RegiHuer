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


class Tierras_Cultivo(models.Model):
    desc_corta = models.CharField(max_length=25, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)

class Plagas(models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)
    tratamiento = models.CharField(max_length=255, blank=True)

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

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    web = models.URLField(blank=True)

    # Python 3
    def __str__(self): 
        return self.usuario.username

class Luz_Necesaria_Cultivo(models.Model):
    cantidad = models.SmallIntegerField()
    descripcion = models.CharField(max_length=255, blank=True)

class Ph_Suelo(models.Model):
    valores = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)

class Temperaturas_Cultivos(models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    valores = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)

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
    )
    familia = models.CharField(max_length=3, choices=FAMILIA)
    nombre_cientifico = models.CharField(max_length=50, blank=True)
    nombre = models.CharField(max_length=50)
    variedad = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)
    tierra = models.ForeignKey(Tierras_Cultivo,on_delete=models.CASCADE, null=True, blank=True)
    tipo_siembra = models.CharField(max_length=1, choices=TIPOS_SIEMBRA)
    luna_siembra = models.CharField(max_length=1, choices=LUNA, null=True, blank=True)
    distancia =  models.FloatField(null=True, blank=True)
    luz = models.ForeignKey(Luz_Necesaria_Cultivo,on_delete=models.CASCADE, null=True, blank=True)
    plagas =   models.ForeignKey(Plagas,on_delete=models.CASCADE,  null=True, blank=True)
    enfermedades  = models.ForeignKey(Enfermedades,on_delete=models.CASCADE, null=True, blank=True)
    semana_siembra_desde= models.CharField(max_length=1, choices=SEMANA, null=True)
    mes_siembra_desde= models.CharField(max_length=3, choices=MES, null=True)
    mes_siembra_hasta = models.CharField(max_length=3, choices=MES, null=True)
    semana_siembra_hasta = models.CharField(max_length=1, choices=SEMANA, null=True)
    dias_germinacion = models.CharField(max_length=50, null=True, blank=True)
    temperaturas = models.ForeignKey(Temperaturas_Cultivos,on_delete=models.CASCADE, null=True, blank=True)
    asociacion_beneficiosa = models.ForeignKey('self',related_name='asosiacion_beneficiosa',  on_delete=models.CASCADE, null=True, blank=True)
    asociacion_no_beneficiosa = models.ForeignKey('self',related_name='asosiacion_no_beneficiosa', on_delete=models.CASCADE, null=True, blank=True)
    ph = models.ForeignKey(Ph_Suelo,on_delete=models.CASCADE, null=True, blank=True)
    imagen = models.ImageField(upload_to='cultivos',blank=True)

    def __str__(self):
        return self.familia +"-"+ self.nombre+"-"+ self.variedad


class Cantero_Cultivos(models.Model):
    cantero = models.ForeignKey(Canteros,on_delete=models.CASCADE)
    cultivo = models.ForeignKey(Cultivos,on_delete=models.CASCADE)
    fechaSiembra = models.DateField(blank=True, null=True)
    fechaCosecha = models.DateField(blank=True, null=True)
    cantidad_sembrada = models.SmallIntegerField(blank=True, null=True)
    observaciones = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.cantero.nombre +"-"+ self.cultivo.nombre


@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()


