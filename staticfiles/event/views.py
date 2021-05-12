from django.shortcuts import render

# from .mocks import Post
from .models import Event
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='compte/acces')
def index(request):
    events = Event.objects.all()
    return render(request, 'next/index.html', {'events': events})


@login_required(login_url='compte/acces')
def show(request, id):
    event = Event.objects.get(pk=id)
    return render(request, 'next/show.html', {'event': event})
