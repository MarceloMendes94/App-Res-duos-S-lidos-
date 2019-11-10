from django import forms
from .models import Cliente, Endereco, Empresa, Motorista, Coleta,ContaBanco,Habilitacao
from django.forms import Form
from django.contrib.auth.models import User

class UserForm(Form):
    first_name  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name   = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email       = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password    = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User


class ColetaForm(Form):
    date_time = forms.DateTimeField(widget=forms.DateTimeField(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Coleta 


class MotoristaForm(Form):
    placa                = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero_habilitacao   = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_habilitacao     = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    validade_habilitacao = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    cpf                  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'data-mask': '000.000.000-00'}))
    data_nascimento      = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Motorista

class ContaBancoForm(Form):
    numConta    = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    agencia     = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ContaBanco

''' # não vejo necessidade, eu fiz e desativei (lewis)
class HabilitacaoForm(Form):
    numero      = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo        = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    validade    = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Habilitacao
'''

class ClienteForm(forms.ModelForm):
    cpf              = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'data-mask': '000.000.000-00'}))
    data_nascimento  = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cliente


class EmpresaForm(Form):
    razao_social = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone     = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cnpj         = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Empresa


class EnderecoForm(Form):
    estado      = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cidade      = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    bairro      = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    logradouro  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cep         = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'data-mask': '00000-000'}))
    numero      = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    referencia  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Endereco


# Como coloco/estendo informações como nome, coisas de pessoa?


