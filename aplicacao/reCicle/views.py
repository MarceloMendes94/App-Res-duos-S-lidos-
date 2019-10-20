from django.shortcuts import render
from .forms import FormMotorista
from .forms import FormCliente
from .forms import FormEndereco
from .models import Cliente
#p = Dodavatel(nazov='Petr', dostupnost=1)
#p.save()

'''
Esse fluxo vai mudar:
/principal/
/motorista/
    /motorista/cadastro/
    /motorista/perfil/
    /motorista/perfil/editar/
    /motorista/selecionar/
    /motorista/coleta/
    /motorista/carteira/
    /motorista/resgate/
    
/cliente/
    /cliente/cadastro/
    /cliente/perfil/
    /cliente/perfil/editar/
    /cliente/agendar/
    /cliente/carteira/
    /cliente/loja/    
'''


def principal(request):
    return render(request, 'reCicle/index.html', {})


def motorista(request):
    return render(request, 'reCicle/motorista.html', {})


def motorista_cadastro(request):
    if request.method == "POST":
        form = FormMotorista(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = FormMotorista(request.POST)
    return render(request, 'reCicle/cadastro_motoristas.html', {'form_motorista': form})


# Redirecionador para tipo de cadastro
def cadastro(request):
    return render(request, 'reCicle/cadastro.html', {})


# cliente


def cliente(request):
    return render(request, 'reCicle/cliente.html', {})


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
        telefone_input= (request.POST.get('telefone'))
        email_input= (request.POST.get('email'))
        senha_input = (request.POST.get('senha'))
        clienteOBJ = Cliente(nome_completo=nome,cpf=cpf_input, tefefone=telefone_input,data_nascimento=data,email=email_input, senha=senha_input, endereco=end)
        clienteOBJ.save()
        #envio = form_cliente.save(commit=False)
        #envio.endereco = end
        #envio.save()
    return render(request, 'reCicle/cadastro_clientes.html',
                  {'form_cliente': form_cliente, 'form_endereco': form_endereco})
