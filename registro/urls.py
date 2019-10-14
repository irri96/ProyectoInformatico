from django.contrib import admin
from django.urls import path,include

from registro.views import signup, salir, registrarme

urlpatterns = [
    path('signup/',signup,name = 'CrearCuenta'),
    path('salir/', salir, name='salir'),
    path('registrarme', registrarme, name='registrarme')
]
