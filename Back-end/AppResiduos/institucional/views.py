from django.shortcuts import render


def principal(request):
    return render(request, 'institucional/index.html', {})


def motorista(request):
    return render(request, 'institucional/motorista.html', {})


def cliente(request):
    return render(request, 'institucional/cliente.html', {})
