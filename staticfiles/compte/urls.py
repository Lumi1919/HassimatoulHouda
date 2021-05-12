from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'compte'
urlpatterns = [
    path('inscription', views.inscriptionPage, name='inscription'),
    path('acces', views.accesPage, name='acces'),
]
