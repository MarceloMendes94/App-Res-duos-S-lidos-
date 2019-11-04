from django.db import models
from django.contrib.auth.models import User

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

#INICIO DA CARTEIRA
class Carteira(models.Model):
    opcoes      = (('m','Motorista'),('c','Cliente'))    
    saldo       = models.DecimalField(decimal_places=2, max_digits=8)
    def __str__(self):
        return str(self.saldo)
# FIM da estrutura de carteira

# INICIO da estrutura de cliente
class Cliente(models.Model):
    usuario =  models.ForeignKey(User,on_delete=models.CASCADE)
    carteira = models.ForeignKey(Carteira,on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco,on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    def __str__(self):
        return self.usuario.email
# FIM da estrutura de cliente

class Motorista(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    carteira = models.ForeignKey(Carteira,on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco,on_delete=models.CASCADE)
    habilitacao = models.CharField(max_length=11)
    placa = models.CharField(max_length=7)

    def __str__(self):
        return self.usuario.email

#INICIO EMPRESA DE COLETA
class Empresa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=14)
    razao_social = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.razao_social + " " + self.cnpj
#FIM EMPRESA DE COLETA






class EmpresaCupom(models.Model):
    nome = models.CharField(max_length=25)
    imagem = models.TextField()

    def __str__(self):
        return self.nome

class Cupom(models.Model):
    empresa = models.ForeignKey(EmpresaCupom, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.empresa.nome + " " + str(self.valor)
