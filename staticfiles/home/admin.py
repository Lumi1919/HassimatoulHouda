from django.contrib import admin
from django.urls import path
from .models import Post

urlpatterns = [
    path('admin/', admin.site.urls),
    admin.site.register(Post)
]

