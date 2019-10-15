from django.contrib.auth import authenticate, login,  get_user_model
from django.shortcuts import render, redirect
from registro.forms import SignUpForm
from django.contrib.auth import logout
from Core.models import User
User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def salir(request):
    logout(request)
    return redirect('home')

def registrarme(request):
    return redirect('CrearCuenta')