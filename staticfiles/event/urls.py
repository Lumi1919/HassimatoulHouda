from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'event'
urlpatterns = [
    path('', views.index, name='activites'),
    url('events/(?P<id>[0-9]+)$', views.show, name='activite'),
]
