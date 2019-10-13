from django.contrib import admin
from Core.models import *

admin.site.register(User)
admin.site.register(Conductor)
admin.site.register(Arrendador)
admin.site.register(Estacionamiento)

# Register your models here.