from django.db import models

# Create your models here.


class Hadara(models.Model):
    titre = models.CharField(max_length=255)

    def __str__(self):
        return self.titre


class Arif(models.Model):
    hadara = models.ForeignKey(Hadara, null=True, blank=True, related_name='arifs', on_delete=models.SET_NULL)
    nom = models.CharField(max_length=255, null=True, blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=12, null=True, blank=True)
    photo = models.ImageField(upload_to='static', null=True, blank=True)

    def __str__(self):
        return self.nom


