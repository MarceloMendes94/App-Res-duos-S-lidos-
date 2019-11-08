#Referencias
#https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Models
#https://www.youtube.com/watch?v=2KqhBkMv7aM
#https://www.youtube.com/watch?v=IJUYdnLvK-A

#Modelo de classe base
#https://www.lucidchart.com/documents/edit/7f4db886-7f9f-4c77-a858-5c4e38aad54a/YGcM5DNywbTK?shared=true

from django.db import models
from django.contrib.auth.models import User


class Empresa(models.Model):
    cnpj = models.CharField(max_length=14)
    razao_social = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.name

class InfoAdicional(models.Model):
    cpf           = models.CharField(max_length=14, help_text='Informe o CPF sem caractéres especiais')
    dt_nascimento = models.DateField(help_text='Informe a sua data de nascimento')

    user          = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.cpf

class Cliente(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True, default=None)

    def __str__(self):
        return "Login Cliente:" + self.email


class Motorista(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True, default=None)

    def __str__(self):
        return "Login Motorista:" + self.email


# INICIO da estrutura de endereço
class Estado(models.Model):
    sigla = models.CharField(max_length=2, help_text='Informe a sigla do seu estado.\nExemplo: ES (Espírito Santo)')

    def __str__(self):
        return self.sigla


class Cidade(Estado):
    nome_cidade = models.CharField(max_length=35, help_text='Informe a cidade onde reside.\nExemplo: Serra')

    def __str__(self):
        return self.nome_cidade


class Bairro(Cidade):
    nome_bairro = models.CharField(max_length=35, help_text='Informe o bairro onde reside.\nExemplo: Manguinhos')

    def __str__(self):
        return self.nome_bairro


class Endereco(Bairro):   # cep e estado com mascara no html
    logradouro = models.CharField(max_length=30, help_text='Exemplo: Alameda, área, avenida, campo, chácara')
    cep        = models.CharField(max_length=8, help_text='Informe o CEP sem caractéres especiais')
    numero     = models.CharField(max_length=4, help_text='Número da residência ou local')
    referencia = models.CharField(max_length=50, help_text='Exemplo: Prédio João Maria, apartamento 201')

    #1:N (Exemplo: uma empresa pode ter mais de um endereço)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.cep+" "+self.numero+" "+self.nome_bairro
# FIM da estrutura de endereço


class Habilitacao(models.Model):
    numero    = models.CharField(max_length=14)
    tipo      = models.CharField(max_length=5) #pode ser choices field
    validade  = models.DateField()

    #Habilitacao é dependente de motorista
    motorista = models.OneToOneField(Motorista, on_delete=models.CASCADE)

    def __str__(self):
        return "Habilitacao" + self.numero


class ContaBanco(models.Model):
    numero_conta = models.IntegerField(max_length=32, help_text='Informe o número da conta para depósito de pagamentos.')
    agencia      = models.IntegerField(max_length=4, help_text='Informe o número da sua agencia.')
    tipo_conta   = models.IntegerField(max_length=3, help_text='Informe o número identificador do tipo de conta.\nExemplo: 500 para poupança.')

    #ContaBanco é dependente de motorista
    motorista    = models.OneToOneField(Motorista, on_delete=models.CASCADE)

    def __str__(self):
        return "Conta bancária:" + self.numero_conta


class Carteira(models.Model):
    TIPO_CARTEIRA   = [('Cliente', 'Cliente'), ('Motorista', 'Motorista')]
    tipo_carteira   = models.CharField(max_length=9, choices=TIPO_CARTEIRA, default=None, )

    #saldoReal pode ficar em branco se a cateira for de cliente, pq ele não tem reais, apenas trashcoin e cupom
    saldo_real      = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    saldo_trashcoin = models.DecimalField(decimal_places=2, max_digits=100, default=0)

    #Carteira nao existe sem Usuario
    #Atenção ao construir uma carteira para usuário, pois existem tipos e o usario Empresa não tem carteira
    user            = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.saldo_real)


class TrashCoin(models.Model):
    taxa  = models.DecimalField(decimal_places=2, max_digits=3)

    def __str__(self):
        return self.saldo

class Cupom(models.Model):
    titulo    = models.CharField(max_length=30, default='')
    SERVICO   = [('Netflix', 'Netflix'), ('Spotify', 'Spotify'), ('Uber', 'Uber')]
    servico   = models.CharField(max_length=7, choices=SERVICO, default=None)
    descricao = models.TextField(max_length=1000, default='')
    valor     = models.IntegerField(default=0)

    def __str__(self):
        return "Cupom:" + self.servico + " de " + self.valor

'''
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
'''
'''
class EmpresaCupom(models.Model):
    nome = models.CharField(max_length=25)
    imagem = models.TextField()

    def __str__(self):
        return self.nome

class Cupom(models.Model):
    empresa = models.ForeignKey(EmpresaCupom, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.empresa.nome + " " + str(self.valor)'''

'''class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=255, help_text='Informe o seu nome completo')
    cpf           = models.CharField(max_length=14, help_text='Informe o CPF sem caractéres especiais')
    dt_nascimento = models.DateField(help_text='Informe a sua data de nascimento')

    #Pessoa depende de Endereço para existir no sistema
    endereco      = models.OneToOneField(Endereco)

    def __str__(self):
        return "CPF"+self.cpf


class Usuario(models.Model):
    email = models.EmailField(max_length=255, help_text='Informe o seu email, ele será o seu login de acesso')
    senha = models.CharField(max_length=12, help_text='Informe uma senha de até 12 caractéres')

    #uma pessoa existe sem usuario, mas um usuario nao existe sem pessoa
    #ou seja, usuario depende de pessoa
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return "Login:" + self.email
'''