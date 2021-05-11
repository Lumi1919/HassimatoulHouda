from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required


@login_required(login_url='compte/acces')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='compte/acces')
def articles(request):
    posts = Post.objects.all()
    return render(request, 'articles.html', {'posts': posts})


@login_required(login_url='compte/acces')
def show(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'show.html', {'post': post})