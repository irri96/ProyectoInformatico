from django.shortcuts import render,redirect
from CreacionEstacionamiento.forms import CrearForm
from Core.models import Estacionamiento, User, Conductor
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
#@user_passes_test(lambda u: u.is_authenticated and u.es_arrendador,login_url='home')
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

def ver_estacionamientos(request,id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return redirect("/")
    try:
        conductor = Conductor.objects.get(user=User(id=user.id))
    except Conductor.DoesNotExist:
        return redirect("/")
    #estacionamientos = []
    #for estacionamiento in Estacionamiento.objects.all():
    #       estacionamientos.append(estacionamiento)
    #
    return render(request, "ver_estacionamientos.html", {"usuario": user})