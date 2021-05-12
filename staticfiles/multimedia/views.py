from django.shortcuts import render
from .models import Audio
from django.contrib.auth.decorators import login_required


@login_required(login_url='compte/acces')
def index(request):
    audios = Audio.objects.all()
    return render(request, 'multi/index.html', {'audios': audios})


@login_required(login_url='compte/acces')
def show(request, id):
    audio = Audio.objects.get(pk=id)
    return render(request, 'multi/show.html', {'audio': audio})