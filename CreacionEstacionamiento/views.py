from django.shortcuts import render,redirect
from CreacionEstacionamiento.forms import CrearForm
from Core.models import Estacionamiento
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
@user_passes_test(lambda u: u.is_authenticated and u.es_arrendador,login_url='home')
def crear(request):
    info = CrearForm()
    if request.method == 'POST':
        info = CrearForm(request.POST or None)
        if info.is_valid():
            info = info.cleaned_data
        arrendador = request.user.arrendador
        publicacion = Estacionamiento(arrendador=arrendador,lat = info.lat,lon=info.lon)
        publicacion.save()
        return redirect('')
    return render(request,'form_creacion_estacionamiento.html',{'form':info})