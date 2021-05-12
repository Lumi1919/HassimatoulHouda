from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='home'),
    path('articles', views.articles, name='articles'),
    url('posts/(?P<id>[0-9]+)$', views.show, name='show'),

]