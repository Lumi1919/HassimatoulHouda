from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'membres'
urlpatterns = [
    path('', views.index, name='hadara'),
    url('(?P<id>[0-9]+)$', views.show, name='arifs'),
]
