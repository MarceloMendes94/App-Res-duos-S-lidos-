from django.shortcuts               import render,redirect
from django.contrib.auth            import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models                        import Carteira, User, Cliente, Endereco
from .forms                         import ClienteForm, EnderecoForm, MotoristaForm, EmpresaForm
from .builder                       import DiretorCliente,DiretorEmpresa,DiretorMotorista
from django.contrib                 import messages
from django.views.decorators.csrf import csrf_protect

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
        #FIELDS CLIENTE
        cpf  = request.POST.get('cpf')
        data_nascimento  = request.POST.get('data_nascimento')        
        DiretorCliente(nome,sobrenome,senha,email,estado,cep,cidade,bairro,logradouro,numero,referencia,cpf,data_nascimento)
    return render(request,'cliente_cadastro.html',{'clienteform':clienteform,'enderecoform':enderecoform})

# motorista
def motorista_cadastro(request):
    motoristaform = MotoristaForm()
    enderecoform = EnderecoForm()
    if request.POST:
        #fields USER
        nome        = request.POST.get('nome')
        sobrenome   = request.POST.get('sobrenome')
        senha       = request.POST.get('password')
        email       = request.POST.get('email')
        #fields ENDERECO
        estado      = request.POST.get('estado')
        cep         = request.POST.get('cep')
        cidade      = request.POST.get('cidade')
        bairro      = request.POST.get('bairro')
        logradouro  = request.POST.get('logradouro')
        numero      = request.POST.get('numero')
        referencia  = request.POST.get('referencia')        
        #fields MOTORISTA
        habilitacao = request.POST.get('habilitacao')
        placa = request.POST.get('placa')
        DiretorMotorista(nome,sobrenome,senha,email,estado,cep,cidade,bairro,logradouro,numero,referencia,habilitacao,placa)
    return render(request, 'motorista_cadastro.html', {'motoristaform': motoristaform, 'enderecoform': enderecoform})

# empresa
def empresa_cadastro(request):
    empresaform = EmpresaForm()
    enderecoform = EnderecoForm()
    if request.POST:
        #fields USER
        nome        = request.POST.get('nome')
        sobrenome   = request.POST.get('sobrenome')
        senha       = request.POST.get('password')
        email       = request.POST.get('email')
        #fields ENDERECO
        estado      = request.POST.get('estado')
        cep         = request.POST.get('cep')
        cidade      = request.POST.get('cidade')
        bairro      = request.POST.get('bairro')
        logradouro  = request.POST.get('logradouro')
        numero      = request.POST.get('numero')
        referencia  = request.POST.get('referencia')        
        #fields EMPRESA
        cnpj  = request.POST.get('cnpj')        
        razao_social  = request.POST.get('razao_social')        
        telefone  = request.POST.get('telefone')        
        #diretor
        DiretorEmpresa(nome,sobrenome,senha,email,estado,cep,cidade,bairro,logradouro,numero,referencia,cnpj,razao_social,telefone)
    return render(request, 'empresa_cadastro.html', {'form_empresa': empresaform, 'enderecoform': enderecoform})





def login_page(request):
    return render(request,'login.html')


def login_submit(request):
    if request.POST:
        user = authenticate(username=request.POST.get('email'),password=request.POST.get('password') )
        if user is not None:
            login(request, user)
            request.session['email'] = user.email      
            return redirect('/cliente/perfil/')
        else:
            messages.error(request, "usuario ou senha invalidos.")

    return render(request,'login.html')

def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def cliente_perfil(request):
    result=User.objects.filter(email=request.session['email'])
    nome=result[0].first_name
    return render(request,'cliente_perfil.html',{'nome':nome})

#@login_required(login_url='/login/')
def agendamento_cadastro(request):
    if request.POST:
        print(request.POST.get('dia'))
        print(request.POST.get('time'))
    return render(request,'agendamento_cadastro.html')


# Redirecionador para tipo de cadastro
def cadastro(request):
    return render(request, 'cadastro.html', {})

# cliente
def cliente(request):
    return render(request, 'cliente.html', {})
