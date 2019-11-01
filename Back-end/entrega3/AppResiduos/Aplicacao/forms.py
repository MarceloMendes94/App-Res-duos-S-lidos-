from django import forms
from .models import Cliente,Endereco, Empresa, Motorista
from django.forms import Form
from django.contrib.auth.models import User

class ClienteForm(Form):
    nome        =    forms.CharField (widget=forms.TextInput (attrs={'class': 'form-control' }))
    sobrenome   =    forms.CharField (widget=forms.TextInput (attrs={'class': 'form-control' }))
    email       =    forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control' }))
    password    =    forms.CharField (widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password' }))

    class Meta:
        model = Cliente

class EnderecoForm(Form):
    estado      =    forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cidade      =    forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    bairro      =    forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    logradouro  =    forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cep         =    forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero      =    forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    referencia  =    forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Endereco

class EmpresaForm(Form):
    razaoSocial =    forms.CharField (widget=forms.TextInput (attrs={'class': 'form-control' }))
    telefone    =    forms.CharField (widget=forms.TextInput (attrs={'class': 'form-control' }))
    cnpj        =    forms.CharField (widget=forms.TextInput (attrs={'class': 'form-control' }))


    class Meta:
        model = Empresa #falta colocar a importação

class MotoristaForm(Form):
    habilitacao        =    forms.CharField (widget=forms.TextInput (attrs={'class': 'form-control' }))
    placa   =    forms.CharField (widget=forms.TextInput (attrs={'class': 'form-control' }))
    email       =    forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control' }))
    password    =    forms.CharField (widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password' }))

    class Meta:
        model = Motorista #falta colocar a importação