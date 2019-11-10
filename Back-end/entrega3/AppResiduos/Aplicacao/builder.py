from .models import *
from django.contrib.auth.models import User

def DiretorEmpresa(nome,sobrenome,senha,email,estado,cep,cidade,bairro,logradouro,numero,referencia,cnpj,razao_social,telefone):
    user = builderUsuario(nome,sobrenome,email,senha)
    end = builderEndereco(estado,cep,cidade,bairro,logradouro,numero,referencia)
    empresa = builderEmpresa(user,end,cnpj,razao_social,telefone)


def DiretorMotorista(nome,sobrenome,senha,email,estado,cep,cidade,bairro,logradouro,numero,referencia,placa,
                         numero_habilitacao,tipo_habilitacao,validade_habilitacao,cpf,data_nascimento, numConta, agencia,tipo_conta):
    user = builderUsuario(nome, sobrenome, email, senha)
    end = builderEndereco(estado, cep, cidade, bairro, logradouro, numero, referencia)
    carteira = builderCarteira(user,tipo_carteira="Motorista") #por ser choices acho que não irá funcionar

    infoAdicional = builderInfoAdicional(user,cpf,data_nascimento)

    motorista = builderMotorista(user,end,placa,carteira)

    contaBanco = builderContaBanco(motorista, numConta, agencia, tipo_conta)
    habilitacao = builderHabilitacao(motorista, numero_habilitacao, tipo_habilitacao, validade_habilitacao)


def DiretorCliente(nome,sobrenome,senha,email,estado,cep,cidade,bairro,logradouro,numero,referencia,cpf,data_nascimento):
    user = builderUsuario(nome, sobrenome, email, senha)
    end = builderEndereco(estado, cep, cidade, bairro, logradouro, numero, referencia)
    carteira = builderCarteira(user,tipo_carteira="Cliente")

    infoAdicional = builderInfoAdicional(user,cpf,data_nascimento)
    cliente = builderCliente(user)


def builderCliente(usuario):
    cliente = Cliente(user= usuario)
    cliente.save()
    return cliente

def builderEndereco(estado, cep, cidade, bairro, logradouro, numero, referencia):
    end = Endereco(sigla=estado, cep=cep, nome_cidade=cidade, nome_bairro=bairro, logradouro=logradouro, numero=numero, referencia=referencia)
    # como que seleciono o tipo se é empresa,cliente,motorista?
    end.save()
    return end

def builderCarteira(user,tipo_carteira):
    carteira = Carteira(saldo_real=0,saldo_trashcoin=0,tipo_carteira= tipo_carteira,user=user)
    carteira.save()
    return carteira

def builderUsuario(nome, sobrenome, email, senha):
    user = User(first_name=nome, username=email, last_name=sobrenome, email=email, password=senha, is_active=True, is_staff=False)
    user.set_password(senha)
    user.save()
    return user

def builderEmpresa(user,endereco,cnpj,razao_social,telefone):
    empresa = Empresa(usuario=user,endereco=endereco,cnpj=cnpj,razao_social=razao_social,telefone=telefone)
    empresa.save()
    return empresa

def builderMotorista(user,endereco,habilitacao,placa,carteira):
    motorista = Motorista(user=user,endereco=endereco,habilitacao=habilitacao,placa=placa,carteira=carteira)
    motorista.save()
    return motorista




def builderInfoAdicional(user,cpf,data_nascimento):
    infoAdicional = InfoAdicional(cpf= cpf, dt_nascimento= data_nascimento, user= user)
    infoAdicional.save()
    return infoAdicional

def builderHabilitacao(motorista,numero,tipo,validade):
    habilitacao = Habilitacao(numero=numero,tipo=tipo,validade=validade,motorista=motorista)
    habilitacao.save()
    return habilitacao

def builderContaBanco(motorista,numero_conta,agencia,tipo_conta):
    contaBanco = ContaBanco(motorista=motorista,numero_conta=numero_conta,agencia=agencia,tipo_conta=tipo_conta)
    contaBanco.save()
    return contaBanco

def builderCupom(titulo,servico,descricao,valor):
    cupom = Cupom(titulo=titulo,servico=servico,descricao=descricao,valor=valor)
    cupom.save()
    return cupom

def builderTrashCoin(taxa):
    ts = TrashCoin(taxa=taxa)
    ts.save()
    return ts

''' # nao foi implementado no models.. acabei deixando comentado aqui porque não tenho certeza (ass luiz)'
def builderColeta(dtHora):
    coleta = Coleta(dtHora=dtHora)
    coleta.save()
    return coleta
'''