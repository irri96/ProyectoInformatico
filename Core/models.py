from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models

class User(AbstractUser):
    #se heredan los campos basicos (nombre, email, pass, etc) de AbstractUser
    es_conductor = models.fields.BooleanField()
    es_arrendador = models.fields.BooleanField()
    rut = models.fields.CharField(max_length=12,unique=True)

class Conductor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    patente = models.fields.CharField(max_length=10)

class Arrendador(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

class Estacionamiento(models.Model):
    duenio = models.ForeignKey(Conductor,on_delete=models.CASCADE)
    #localizacion como punto en srid 4326 (GPS)
    localizacion = models.PointField()

class Valoracion(models.Model):
    emisor = models.ForeignKey(User,on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, on_delete=models.CASCADE)
    valoracion = models.fields.IntegerField()
    comentario = models.fields.CharField(max_length=140)




# Create your models here.
