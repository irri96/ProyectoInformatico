
from django.contrib import admin
from django.urls import path,include
from CreacionEstacionamiento.views import crear, ver_estacionamientos, parking
urlpatterns = [
    path('crear/',crear,name = 'CrearEstacionamiento'),
    path('ver_estacionamientos/<int:id>', ver_estacionamientos, name = 'VerEstacionamientos'),
    path('parking/', parking, name = 'parking'),
]
