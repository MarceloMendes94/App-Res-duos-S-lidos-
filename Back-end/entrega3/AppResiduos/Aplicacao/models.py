from django.db import models
from django.contrib.auth.models import User


# documentação https://docs.djangoproject.com/en/2.2/topics/db/models/
# INICIO da estrutura de endereço        
class Estado(models.Model):
    sigla = models.CharField(max_length=2)
    def __str__(self):
        return self.sigla

class Cidade(Estado):
    nome_cidade = models.CharField(max_length=35)
    def __str__(self):
        return self.nome_cidade

class Bairro(Cidade):
    nome_bairro = models.CharField(max_length=35)
    def __str__(self):
        return self.nome_bairro

class Endereco(Bairro):   # cep e estado com mascara no html
    logradouro = models.TextField()
    cep        = models.CharField(max_length=8)
    numero     = models.CharField(max_length=4)
    referencia = models.TextField()
    def __str__(self):
        return self.cep+" "+self.numero+" "+self.nome_bairro
# FIM da estrutura de endereço  


# INICIO da estrutura de carteira
class Carteira(models.Model):
    saldo = models.DecimalField(decimal_places=2, max_digits=8)
    def __str__(self):
        return str(self.saldo)
# FIM da estrutura de carteira


# documentação sobre tipo USER https://docs.djangoproject.com/en/2.2/ref/contrib/auth/
# INICIO da estrutura de cliente
class Cliente(models.Model):
    usuario =  models.ForeignKey(User,on_delete=models.CASCADE)
    carteira = models.ForeignKey(Carteira,on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco,on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario.email
# FIM da estrutura de cliente