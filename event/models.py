from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='static', null=True, blank=True)
    photo1 = models.ImageField(upload_to='static', null=True, blank=True)
    photo2 = models.ImageField(upload_to='static', null=True, blank=True)
    photo3 = models.ImageField(upload_to='static', null=True, blank=True)
    photo4 = models.ImageField(upload_to='static', null=True, blank=True)

    def __str__(self):
        return self.title


# Create your models here.
