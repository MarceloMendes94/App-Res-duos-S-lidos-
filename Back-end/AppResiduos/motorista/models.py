from django.db import models

# Create your models here.
class Motorista(models.Model):
    nome            = models.CharField(max_length=35)
    cpf             = models.CharField(max_length=11)
    placa           = models.CharField(max_length=8)
    habilitacao     = models.CharField(max_length=11)
    dt_nascimento   = models.DateField(null=True, blank=True)
    nada_consta     = models.BooleanField()

