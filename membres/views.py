from django.shortcuts import render
# from .mocks import Arif
from .models import Arif
from django.contrib.auth.decorators import login_required


@login_required(login_url='compte/acces')
def index(request):
    arifs = Arif.objects.all()
    return render(request, 'member/index.html', {'arifs': arifs})


@login_required(login_url='compte/acces')
def show(request, id):
    arif = Arif.objects.get(pk=id)
    return render(request, 'member/show.html', {'arif': arif})
