from .models import *


def fabricaUsuario(escolha,nome,sobrenome,email,senha,estado,cep,cidade,bairro,logradouro,numero,referencia,cpf_hab_cnpj):
    end = builderEndereco(estado,cep,cidade,bairro,logradouro,numero,referencia)
    user = builderUsuario(nome,sobrenome,email,senha)
    carteira = builderCarteira()
        
def builderCliente:
    cliente  = Cliente(usuario=usuario,carteira=carteira,endereco=end)
    cliente.save()
    
def builderMotorista:

def builderEmpresa:

def builderEndereco(estado,cep,cidade,bairro,logradouro,numero,referencia):
    end=Endereco(sigla=estado,cep=cep,nome_cidade=cidade,nome_bairro=bairro,logradouro=logradouro,numero=numero,referencia=referencia)
    end.save()
    return end

def builderCarteira():
    carteira = Carteira(saldo=0)
    carteira.save()
    return carteira

def builderUsuario(nome,sobrenome,email,senha):
    user = User(first_name = nome,username = email, last_name = sobrenome, email = email, password = senha, is_active = True,is_staff=False)
    user.set_password(senha)
    user.save()
    return user