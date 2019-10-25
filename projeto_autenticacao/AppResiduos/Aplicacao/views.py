from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from .forms import ClienteForm,EnderecoForm, loginForm 
from .models import Endereco, Carteira,Cliente
from django.contrib.auth.models import User
from django.contrib import messages


def principal(request):
    return render(request,'Aplicacao/index.html',{})

def cadastro_cliente(request):    
    formulario_endereco = EnderecoForm()
    formulario_cliente = ClienteForm()
    if request.method == "GET":    
        return render(request,'Aplicacao/cadastro_cliente.html',{'formulario_endereco':formulario_endereco , 'formulario_cliente':formulario_cliente })
    if request.method == "POST":
        #insert here your code
        carteira = _instanciarCarteira(request)
        carteira.save()
        endereco = _instanciarEndereco(request)
        endereco.save()
        cliente = _instanciarCliente(request,carteira,endereco)
        cliente.save()

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        # print('criando usuario')
        # user = User.objects.create_user(name=nome,email= email, password=senha)
        # print(user)
        # print('Salvando')
        # user.save()

        #redimensionar  para pagina de login
    return render(request,'Aplicacao/cadastro_cliente.html',{'formulario_endereco':formulario_endereco , 'formulario_cliente':formulario_cliente })            

def login(request):
    form=loginForm()
    if request.method=='POST':
        username = request.POST['email']
        password = request.POST['password']
        print('username: ',username)
        print('password: ',password)

        user = authenticate(username= username, password = password)
        print(user)
        if user is not None:
            print("acho q deu boa")
            login(request,user)
        else:
            print("DEU NAO")
            messages.error(request,"usuario ou senha invalidos.")
        
    return render(request,'Aplicacao/login.html',{'form':form})


#funções de auxilio ao código limpo
def _instanciarEndereco(request):
    estado = request.POST.get('estado')
    bairro = request.POST.get('bairro')
    cidade = request.POST.get('cidade')
    logradouro =request.POST.get('logradouro')
    cep =request.POST.get('cep')
    numero =request.POST.get('numero')
    referencia =request.POST.get('referencia')
    return Endereco(sigla=estado,nome_bairro=bairro,nome_cidade=cidade,logradouro=logradouro,cep=cep,referencia = referencia, numero=numero)

def _instanciarCarteira(request):
    return Carteira(saldo=0)

def _instanciarCliente(request,carteira,endereco):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    senha =request.POST.get('password')
    return Cliente(first_name=nome,last_name=sobrenome,email=email,username=email,password=senha,is_active=True,is_staff=False,is_superuser=False,carteira=carteira,endereco=endereco)
