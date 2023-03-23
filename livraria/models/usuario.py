from django.db import models
from django.contrib.auth.models import AbstractUser
from uploader.models import Image

class Usuario(AbstractUser):
    foto = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=True,
    )
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)