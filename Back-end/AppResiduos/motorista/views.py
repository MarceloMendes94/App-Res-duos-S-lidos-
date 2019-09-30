from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def motorista_crud(request):
    return render(request,'motorista/motorista.html',{})

#def motorista_cad(request):
#    return render(request,'motorista/cadastro_motorista.html',{})

def novo_motorista(request):
    if request.method == "POST":
       form = PostForm(request.POST)

       if form.is_valid(): 
           motorista                 = form.save(commit=False)
           
           motorista.nome            = form['nome'].value()
           motorista.cpf             = form['cpf'].value()
           motorista.placa           = form['placa'].value()
           print(" \n\n \n  {}     ".format(motorista.placa))
           motorista.habilitacao     = form['habilitacao'].value()
          # motorista.dt_nascimento   = form['dt_nascimneto'].value()
           motorista.nada_consta     = True
           motorista.save()
    else:   
        form = PostForm()#proprio do django

    return render(request, 'motorista/cadastro_motorista.html', {'form': form})    
  