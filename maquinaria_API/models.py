from pyexpat import model
from django.db import models

# Create your models here.
class Maquina(models.Model):
    nombre = models.CharField(max_length=255)
    clase = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    dado_de_baja = models.BooleanField(default=False)