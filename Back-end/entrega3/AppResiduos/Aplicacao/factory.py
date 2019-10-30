from .models import *



def fabricaUsuario(escolha,nome,sobrenome,email,senha,estado,cep,cidade,bairro,logradouro,numero,referencia,cpf_hab_cnpj):
    end=builderEndereco(estado,cep,cidade,bairro,logradouro,numero,referencia)

    user=_usuario(nome,sobrenome,email,senha)
    user.save()
        
def builderCliente:
    
def builderMotorista:

def builderEmpresa:

def builderEndereco(estado,cep,cidade,bairro,logradouro,numero,referencia):
        end=Endereco(sigla=estado,cep=cep,nome_cidade=cidade,nome_bairro=bairro,logradouro=logradouro,numero=numero,referencia=referencia)
        end.save()
        return end
#funções implicitas
def _carteira():
    return Carteira(saldo=0)

def _usuario(nome,sobrenome,email,senha):
    user = User(first_name = nome,username = email, last_name = sobrenome, email = email, password = senha, is_active = True,is_staff=False)
    user.set_password(senha)
    return user

def _endereco(estado,cep,cidade,bairro,logradouro,numero,referencia):





    