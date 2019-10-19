from django.shortcuts import render, redirect
from .forms import FormMotorista, FormCliente, FormEndereco, FormLogin
from core.models import Cliente, Cupom

'''
/principal/
/login/
    /motorista/cadastro/*
    /motorista/perfil/
    /motorista/perfil/editar/
    /motorista/selecionar/
    /motorista/coleta/
    /motorista/carteira/
    /motorista/resgate/
    
    /cliente/cadastro/*
    /cliente/perfil/*
    /cliente/perfil/editar/
    /cliente/agendar/
    /cliente/carteira/
    /cliente/loja/*    
'''


# trabalhando a autenticação


def principal(request):
    return render(request, 'core/index.html', {})


def login(request):
    form_login = FormLogin(request.POST)
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        result = Cliente.objects.filter(email=email, senha=senha)
        if (len(result)):
            request.session['auth_email'] = email
            request.session['auth_senha'] = senha
            request.session['auth_tokken'] = True
            return redirect('/cliente/perfil/')
        else:
            request.session['auth_email'] = 0
            request.session['auth_senha'] = 0
            request.session['auth_tokken'] = 0
            print("erro")

    return render(request, 'core/login.html', {"form_login": form_login})


# motorista
def motorista(request):
    return render(request, 'core/motorista.html', {})


def motorista_cadastro(request):
    form = FormMotorista(request.POST)
    if request.method == "POST":
        form = FormMotorista(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = FormMotorista(request.POST)
    return render(request, 'core/cadastro_motoristas.html', {'form': form})


# Redirecionador para tipo de cadastro
def cadastro(request):
    return render(request, 'core/cadastro.html', {})


# cliente
def cliente(request):
    return render(request, 'core/cliente.html', {})


def cliente_cadastro(request):
    form_cliente = FormCliente(request.POST)
    form_endereco = FormEndereco(request.POST)
    if form_endereco.is_valid() and form_cliente:
        form_endereco.save(commit=False)
        end = form_endereco.save()
        # Dados pessoais
        nome = (request.POST.get('nome_completo'))
        data = (request.POST.get('data_de_nascimento'))
        cpf_input = (request.POST.get('cpf'))
        telefone_input = (request.POST.get('telefone'))
        email_input = (request.POST.get('email'))
        senha_input = (request.POST.get('senha'))
        clienteOBJ = Cliente(nome_completo=nome, cpf=cpf_input, tefefone=telefone_input, data_nascimento=data,
                             email=email_input, senha=senha_input, endereco=end)
        clienteOBJ.save()
    return render(request, 'core/cadastro_clientes.html',
                  {'form_cliente': form_cliente, 'form_endereco': form_endereco})


def cliente_autenticado(request):
    # print(request.session['auth_email'])    print(request.session['auth_senha'])    print(request.session['auth_tokken'])
    if request.session['auth_email'] != 0 and request.session['auth_senha'] != 0 and request.session['auth_tokken'] != 0:
        return render(request, 'core/cliente_perfil.html', {})
    else:
        print('erro gambi')
        form_login = FormLogin(request.POST)
        return render(request, 'core/login.html', {"form_login": form_login})
    return render(request, 'core/index.html', {})


def cliente_loja(request):
    result = Cupom.objects.all()
    print(result)
    return render(request, 'core/cliente_loja.html', {"result": result})
