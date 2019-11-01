from django.shortcuts               import render,redirect
from django.contrib.auth            import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models                        import Carteira, User, Cliente, Endereco
from .forms                         import ClienteForm, EnderecoForm, MotoristaForm, EmpresaForm
from .factory                       import *
from django.contrib                 import messages

def index(request):
    return render(request,'index.html')

def cliente_cadastro(request): 
    clienteform  = ClienteForm()
    enderecoform = EnderecoForm()
    if request.POST:
        #user fields
        nome        = request.POST.get('nome')
        sobrenome   = request.POST.get('sobrenome')
        senha       = request.POST.get('password')
        email       = request.POST.get('email')
        #endereco fields
        estado      = request.POST.get('estado')
        cep         = request.POST.get('cep')
        cidade      = request.POST.get('cidade')
        bairro      = request.POST.get('bairro')
        logradouro  = request.POST.get('logradouro')
        numero      = request.POST.get('numero')
        referencia  = request.POST.get('referencia')
        #construindo objetos
        #end         = _endereco(estado,cep,cidade,bairro,logradouro,numero,referencia)        
        #end.save()
        #carteira    = _carteira()
        #carteira.save()
        #usuario     = _usuario(nome,sobrenome,email,senha)
        #usuario.save()
        #cliente     = Cliente(usuario=usuario,carteira=carteira,endereco=end)
        #cliente.save()
        # fabricaUsuario(escolha=1,nome=nome,sobrenome=sobrenome,email=email,senha=senha,estado=estado,cep=cep,cidade=cidade,bairro=bairro,logradouro=logradouro,numero=numero,referencia=referencia,cpf_hab_cnpj=1)
    return render(request,'cliente_cadastro.html',{'clienteform':clienteform,'enderecoform':enderecoform})

def login_page(request):
    return render(request,'login.html')

def login_submit(request):
    if request.POST:
        print(request.POST.get('email'))
        print(request.POST.get('password'))
        user = authenticate(username=request.POST.get('email'),password=request.POST.get('password') )
        print(user)
        if user is not None:
            login(request, user)
            return render(request,'perfil.html')
        else:
            messages.error(request, "usuario ou senha invalidos.")
    return render(request,'login.html')

def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def cliente_perfil(request):
    return render(request,'perfil.html')

# Redirecionador para tipo de cadastro
def cadastro(request):
    return render(request, 'cadastro.html', {})

# motorista
def motorista_cadastro(request):
    motoristaform = MotoristaForm()
    enderecoform = EnderecoForm()
    # if request.POST:
    #     # user fields
    #     nome = request.POST.get('nome')
    #     sobrenome = request.POST.get('sobrenome')
    #     senha = request.POST.get('password')
    #     email = request.POST.get('email')
    #     # endereco fields
    #     estado = request.POST.get('estado')
    #     cep = request.POST.get('cep')
    #     cidade = request.POST.get('cidade')
    #     bairro = request.POST.get('bairro')
    #     logradouro = request.POST.get('logradouro')
    #     numero = request.POST.get('numero')
    #     referencia = request.POST.get('referencia')
    #     # construindo objetos
    #     # end         = _endereco(estado,cep,cidade,bairro,logradouro,numero,referencia)
    #     # end.save()
    #     # carteira    = _carteira()
    #     # carteira.save()
    #     # usuario     = _usuario(nome,sobrenome,email,senha)
    #     # usuario.save()
    #     # cliente     = Cliente(usuario=usuario,carteira=carteira,endereco=end)
    #     # cliente.save()
    #     fabricaUsuario(escolha=1, nome=nome, sobrenome=sobrenome, email=email, senha=senha, estado=estado, cep=cep,
    #                    cidade=cidade, bairro=bairro, logradouro=logradouro, numero=numero, referencia=referencia,
    #                    cpf_hab_cnpj=1)
    return render(request, 'motorista_cadastro.html', {'motoristaform': motoristaform, 'enderecoform': enderecoform})

# motorista
def empresa_cadastro(request):
    empresaform = EmpresaForm()
    enderecoform = EnderecoForm()
    # if request.POST:
    #     # user fields
    #     nome = request.POST.get('nome')
    #     sobrenome = request.POST.get('sobrenome')
    #     senha = request.POST.get('password')
    #     email = request.POST.get('email')
    #     # endereco fields
    #     estado = request.POST.get('estado')
    #     cep = request.POST.get('cep')
    #     cidade = request.POST.get('cidade')
    #     bairro = request.POST.get('bairro')
    #     logradouro = request.POST.get('logradouro')
    #     numero = request.POST.get('numero')
    #     referencia = request.POST.get('referencia')
    #     # construindo objetos
    #     # end         = _endereco(estado,cep,cidade,bairro,logradouro,numero,referencia)
    #     # end.save()
    #     # carteira    = _carteira()
    #     # carteira.save()
    #     # usuario     = _usuario(nome,sobrenome,email,senha)
    #     # usuario.save()
    #     # cliente     = Cliente(usuario=usuario,carteira=carteira,endereco=end)
    #     # cliente.save()
    #     fabricaUsuario(escolha=1, nome=nome, sobrenome=sobrenome, email=email, senha=senha, estado=estado, cep=cep,
    #                    cidade=cidade, bairro=bairro, logradouro=logradouro, numero=numero, referencia=referencia,
    #                    cpf_hab_cnpj=1)
    return render(request, 'empresa_cadastro.html', {'form_empresa': empresaform, 'enderecoform': enderecoform})

# cliente
def cliente(request):
    return render(request, 'cliente.html', {})


#funções implicitas
def _carteira():
    return Carteira(saldo=0)

def _usuario(nome,sobrenome,email,senha):
    user = User(first_name = nome,username = email, last_name = sobrenome, email = email, password = senha, is_active = True,is_staff=False)
    user.set_password(senha)
    return user

def _endereco(estado,cep,cidade,bairro,logradouro,numero,referencia):
    return Endereco(sigla=estado,cep=cep,nome_cidade=cidade,nome_bairro=bairro,logradouro=logradouro,numero=numero,referencia=referencia)