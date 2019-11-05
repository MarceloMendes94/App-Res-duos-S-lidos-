from django.db import models
from django.contrib.auth.models import User

#Referencias
#https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Models

#Modelo de classe base
#https://www.lucidchart.com/documents/edit/7f4db886-7f9f-4c77-a858-5c4e38aad54a/YGcM5DNywbTK?shared=true

# INICIO da estrutura de endereço        
class Estado(models.Model):
    #da pra usar choices aqui
    #consulte: https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-options
    sigla = models.CharField(max_length=2, help_text='Informe a sigla do seu estado.\nExemplo: ES (Espírito Santo)')

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

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=100)
    cpf           = models.CharField(max_length=14)
    dt_nascimento = models.DateField()

    def __str__(self):
        return self.nome_completo +" "+ self.cpf

class Usuario(Pessoa):
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=12)

    def __str__(self):
        return "Login:" + self.email

class Cliente(Usuario):

    def __str__(self):
        return "Login Cliente:" + self.email

class Motorista(Usuario):
    placa       = models.CharField(max_length=8)
    nada_consta = models.BooleanField(None)


class Habilitacao(models.Model):
    numero   = models.CharField(max_length=14)
    tipo     = models.CharField(max_length=5)
    validade = models.DateField()

    def __str__(self):
        return "Habilitacao"+self.numero

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
