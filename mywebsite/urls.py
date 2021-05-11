from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('home.urls')),
    path('compte/', include('compte.urls')),
    path('multimedia/', include('multimedia.urls')),
    path('membres/', include('membres.urls')),
    path('event/', include('event.urls')),
    path('admin/', admin.site.urls)
]
