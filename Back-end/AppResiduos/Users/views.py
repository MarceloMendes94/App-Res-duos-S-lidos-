from django.shortcuts import render
from .forms import FormMotorista
from .forms import FormCliente
from .forms import FormEndereco

def motorista_cadastro(request):
    if request.method == "POST":
        form = FormMotorista(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = FormMotorista(request.POST)
    return render(request, 'Users/cadastro_motoristas.html', {'form':form})


def cliente_cadastro(request):
    form_cliente = FormCliente(request.POST)
    form_endereco = FormEndereco(request.POST)
    if form_endereco.is_valid() and form_cliente:
        form_endereco.save(commit=False)
        end= form_endereco.save()
        envio=form_cliente.save(commit=False)
        envio.endereco = end
        envio.save()
    return render(request, 'Users/cadastro_clientes.html', {'form_cliente': form_cliente, 'form_endereco': form_endereco})





