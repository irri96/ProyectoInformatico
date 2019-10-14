from django.contrib import admin
from django.urls import path,include

from registro.views import signup

urlpatterns = [
    path('signup/',signup,name = 'CrearCuenta'),
]
