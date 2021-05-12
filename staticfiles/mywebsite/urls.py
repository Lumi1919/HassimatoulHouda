from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url


urlpatterns = [
    path('', include('home.urls')),
    path('compte/', include('compte.urls')),
    path('multimedia/', include('multimedia.urls')),
    path('membres/', include('membres.urls')),
    path('event/', include('event.urls')),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL)
