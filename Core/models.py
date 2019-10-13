from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #se heredan los campos basicos (nombre, email, pass, etc) de AbstractUser
    es_conductor = models.fields.BooleanField(default=False)
    es_arrendador = models.fields.BooleanField(default=False)
    rut = models.fields.CharField(max_length=12,unique=True)

class Conductor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    patente = models.fields.CharField(max_length=10)

class Arrendador(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

class Estacionamiento(models.Model):
    duenio = models.ForeignKey(Conductor,on_delete=models.CASCADE)
    #localizacion como punto en srid 4326 (GPS)
    lat = models.DecimalField(max_digits=10,decimal_places=7)
    lon = models.DecimalField(max_digits=10, decimal_places=7)

# class Valoracion(models.Model):
#     emisor = models.ForeignKey(User,on_delete=models.CASCADE,related_name="emisor")
#     receptor = models.ForeignKey(User, on_delete=models.CASCADE,related_name="receptor")
#     valoracion = models.fields.IntegerField()
#     comentario = models.fields.CharField(max_length=140)

class Oferta(models.Model):
    estacionamiento = models.ForeignKey(Estacionamiento,on_delete=models.CASCADE)
    hora_inicio = models.DateTimeField()
    hora_final = models.DateTimeField()
    plazas_libres = models.IntegerField()

class Reserva(models.Model):
    oferta = models.ForeignKey(Oferta,on_delete=models.CASCADE)
    conductor = models.ForeignKey(Conductor,on_delete=models.CASCADE)
    estado = models.IntegerField()


# Create your models here.
