# from django.contrib.auth.models import User
# from .models import *
#
#
#
# class BuilderEndereco(estado,cep,cidade,bairro,logradouro,numero,referencia):
# 	def _init_(self):
# 		self.end=Endereco()
#
# 	def builderAll(self)
# 		self.end=Endereco(sigla=estado,cep=cep,nome_cidade=cidade,nome_bairro=bairro,logradouro=logradouro,numero=numero,referencia=referencia)
# 	def builderSave(self)
# 		self.end.save()
#
# class diretorEndereco(estado,cep,cidade,bairro,logradouro,numero,referencia):
#
#     def __init__(estado,cep,cidade,bairro,logradouro,numero,referencia):
#         self.end=BuilderEndereco(estado,cep,cidade,bairro,logradouro,numero,referencia)
#
#
#     def builder():
#         self.end.builderAll()
# 		self.end.builderSave()
# 		return end
#
#
# def fabricaUsuario(escolha,nome,sobrenome,email,senha,estado,cep,cidade,bairro,logradouro,numero,referencia,cpf_hab_cnpj):
#     director=diretorEndereco(estado,cep,cidade,bairro,logradouro,numero,referencia)
# 	end = director.builder()
#
#     user = builderUsuario(nome,sobrenome,email,senha)
#     carteira = builderCarteira()
#
#     if(escolha==1):
#         builderCliente(usuario=user,carteira=carteira,endereco=end)
#
#
#
# def diretorEndereco()
# def builderCliente(usuario,carteira,endereco):
#     cliente  = Cliente(usuario=usuario,carteira=carteira,endereco=endereco)
#     cliente.save()
#
# #def builderMotorista():
#
# #def builderEmpresa():
#
# def builderEndereco(estado,cep,cidade,bairro,logradouro,numero,referencia):
#     end=Endereco(sigla=estado,cep=cep,nome_cidade=cidade,nome_bairro=bairro,logradouro=logradouro,numero=numero,referencia=referencia)
#     end.save()
#     return end
#
# def builderCarteira():
#     carteira = Carteira(saldo=0)
#     carteira.save()
#     return carteira
#
# def builderUsuario(nome,sobrenome,email,senha):
#     user = User(first_name = nome,username = email, last_name = sobrenome, email = email, password = senha, is_active = True,is_staff=False)
#     user.set_password(senha)
#     user.save()
#     return user