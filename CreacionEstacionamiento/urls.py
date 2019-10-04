
from django.contrib import admin
from django.urls import path,include
from CreacionEstacionamiento.views import crear
urlpatterns = [
    path('crear/',crear,name = 'CrearEstacionamiento')
]
