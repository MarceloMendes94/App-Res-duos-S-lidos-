from django.shortcuts               import render,redirect
from django.contrib.auth            import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models                        import Carteira, User, Cliente, Endereco
from .forms                         import ClienteForm, EnderecoForm 

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
        end         = _endereco(estado,cep,cidade,bairro,logradouro,numero,referencia)        
        end.save()
        carteira    = _carteira()
        carteira.save()
        usuario     = _usuario(nome,sobrenome,email,senha)
        usuario.save()
        cliente     = Cliente(usuario=usuario,carteira=carteira,endereco=end)
        cliente.save()
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
    return render(request,'login.html')

def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def cliente_perfil(request):
    return render(request,'perfil.html')



#funções implicitas
def _carteira():
    return Carteira(saldo=0)

def _usuario(nome,sobrenome,email,senha):
    user = User(first_name = nome,username = email, last_name = sobrenome, email = email, password = senha, is_active = True,is_staff=False)
    user.set_password(senha)
    return user

def _endereco(estado,cep,cidade,bairro,logradouro,numero,referencia):
    return Endereco(sigla=estado,cep=cep,nome_cidade=cidade,nome_bairro=bairro,logradouro=logradouro,numero=numero,referencia=referencia)