from django.db import models

'''

'''


class Estado(models.Model):
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return


class Cidade(Estado):
    nome_cidade = models.CharField(max_length=30)


class Bairro(Cidade):
    nome_bairro = models.CharField(max_length=30)


class Endereco(Bairro):
    cep = models.CharField(max_length=8)
    numero = models.CharField(max_length=5)
    logradouro = models.CharField(max_length=50)
    referencia = models.TextField()

    def __str__(self):
        return self.cep + " " + self.nome_bairro + " " + self.nome_cidade + " " + self.sigla


class Usuario(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=180)


class Motorista(Usuario):
    habilitacao = models.CharField(max_length=11)
    placa = models.CharField(max_length=7)


class Cliente(Usuario):
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    nome_completo = models.TextField()
    tefefone = models.CharField(max_length=11)
    data_nascimento = models.DateField()
