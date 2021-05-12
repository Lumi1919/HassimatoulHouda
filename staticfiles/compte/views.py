from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreerUtilisateur
from django.contrib.auth import authenticate, login, logout


# Create your models here.


def inscriptionPage(request):
    form = CreerUtilisateur()
    if request.method == 'POST':
        form = CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'gestion/acces.html')
    context = {'form': form}
    return render(request, 'gestion/inscription.html', context)


def accesPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')
    return render(request, 'gestion/acces.html', context)


def logoutUser(request):
    logout(request)
    return redirect('acces')
