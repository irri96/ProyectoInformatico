from django.urls import include, path

from .views import Inicio

urlpatterns = [
    path('', Inicio.home, name='home'),

    #path('registro/conductor',Inicio.RegistroConductor),
    #   path('registro/arrendador',Inicio.RegistroArrendador),
]