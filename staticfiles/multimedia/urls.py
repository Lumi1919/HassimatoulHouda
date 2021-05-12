from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'multimedia'
urlpatterns = [
    path('', views.index, name='multiindex'),
    url('(?P<id>[0-9]+)$', views.show, name='multishow'),

]
