from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(AbstractUser):
    direccion = models.CharField(max_length=300, null=True, blank=True)
    telefono = models.CharField(max_length=12, null=True, blank=True)
    documentoIdentidad = models.CharField(max_length=30, null=True, blank=True, help_text=("Si es menor de edad, deje el espacio en blanco"))

    def save(self, *args, **kwargs):
        if not self.documentoIdentidad:
            self.documentoIdentidad = 'Menor de edad'

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
# Create your models here.
