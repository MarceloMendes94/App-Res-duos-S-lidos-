from .models import *

def DiretorEmpresa(nome,sobrenome,senha,email,estado,cep,cidade,bairro,logradouro,numero,referencia,cnpj,razao_social,telefone)
    user = builderUsuario(nome,sobrenome,email,senha)
    end = builderEndereco(estado,cep,cidade,bairro,logradouro,numero,referencia)
    empresa = builderEmpresa(user,end,cnpj,razao_social,telefone)


def DiretorMotorista(nome,sobrenome,senha,email,estado,cep,cidade,bairro,logradouro,numero,referencia,habilitacao,placa)
    user = builderUsuario(nome, sobrenome, email, senha)
    end = builderEndereco(estado, cep, cidade, bairro, logradouro, numero, referencia)
    carteira = builderCarteira()
    motorista = builderMotorista(nome,end,habilitacao,placa,carteira)


def DiretorCliente(nome, sobrenome, senha, email, estado, cep, cidade, bairro, logradouro, numero, referencia, cpf, data_nascimento)
    user = builderUsuario(nome, sobrenome, email, senha)
    end = builderEndereco(estado, cep, cidade, bairro, logradouro, numero, referencia)
    carteira = builderCarteira()
    cliente = builderCliente(user,end,cpf, data_nascimento,carteira)


def builderCliente(usuario, endereco,cpf, data_nascimento,carteira):
    cliente = Cliente(usuario=usuario, carteira=carteira, endereco=endereco,cpf=cpf,data_nascimento=data_nascimento)
    cliente.save()
    return cliente

def builderEndereco(estado, cep, cidade, bairro, logradouro, numero, referencia):
    end = Endereco(sigla=estado, cep=cep, nome_cidade=cidade, nome_bairro=bairro, logradouro=logradouro, numero=numero, referencia=referencia)
    end.save()
    return end

def builderCarteira():
    carteira = Carteira(saldo=0)
    carteira.save()
    return carteira

def builderUsuario(nome, sobrenome, email, senha):
    user = User(first_name=nome, username=email, last_name=sobrenome, email=email, password=senha, is_active=True,
                is_staff=False)
    user.set_password(senha)
    user.save()
    return user

def builderEmpresa(user,endereco,cnpj,razao_social,telefone):
    empresa = Empresa(usuario=user,endereco=endereco,cnpj=cnpj,razao_social=razao_social,telefone=telefone)
    empresa.save()
    return empresa

def builderMotorista(user,endereco,habilitacao,placa,carteira)
    motorista = Motorista(user=user,endereco=endereco,habilitacao=habilitacao,placa=placa,carteira=carteira)
    motorista.save()
    return motorista