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



#INICIOCOLETAGEM
class Residuo(models.Model):
    nome_residuo = models.CharField(max_length=35) 
    valor_kilo   = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return self.nome_residuo

class Coleta(models.Model):
    cliente     = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    aguardando  = models.BooleanField() 
    def __str__(self):         
         #+" "+self.numero+" "+self.nome_bairro
        return  "CEP:"+self.cliente.endereco.cep+" NUMERO:"+self.cliente.endereco.numero+" BAIRRO:"+self.cliente.endereco.bairro.nome_bairro+" CIDADE:"+self.cliente.endereco.cidade.nome_cidade

class Pesagem(models.Model):
    motorista   = models.ForeignKey(Motorista,  on_delete=models.CASCADE)
    cliente     = models.ForeignKey(Cliente,    on_delete=models.CASCADE)
    residuo     = models.ForeignKey(Residuo,    on_delete=models.CASCADE)
    peso        = models.DecimalField(max_digits=8, decimal_places=3)
    data_hora   = models.DateTimeField()
    def __str__(self):
        return self.cliente.endereco.cep+" "+str(self.data_hora)+"  PESO:"+str(self.peso)+"  MATERIAL:"+self.residuo.nome_residuo
#FIMCOLETAGEM


#   INICIO CUPOMS
class EmpresaCupom(models.Model):
    nome = models.CharField(max_length=25)
    imagem = models.TextField()

    def __str__(self):
        return self.nome

class Cupom(models.Model):
    empresa = models.ForeignKey(EmpresaCupom, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=4, decimal_places=2)
    descricao = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.empresa.nome + " " + str(self.valor)
#   FIM CUPOMS

class ComprovanteEntrega(models.Model):
    #um "protocolo singleton", mas ele identifica a entrega de um "motorista" que aconteceu em "tal dia", e gerou tal "valor de pagamento"
    #data_hora = models.DateTimeField(auto_now_add=True)
    mes = models.DecimalField(max_digits=2, decimal_places=0)
    nome_empresa = models.CharField(max_length=30, default="")
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    #usar o id como "protocolo singleton"


    #motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome_empresa


class TransacaoMensal(models.Model):
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField(auto_now_add=True)
    nome_empresa = models.CharField(max_length=30, default="")
    #empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    #protocolos

    
    comprovante = models.ForeignKey(ComprovanteEntrega, on_delete=models.DO_NOTHING, null=True)
    def __str__(self):
        pass


