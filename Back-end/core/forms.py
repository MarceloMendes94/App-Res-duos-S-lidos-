from django import forms
from django.forms import Form

from .models import Motorista
from .models import Cliente
from .models import Endereco
from .models import EmpresaReciclagem


class FormMotorista(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ('habilitacao', 'placa', 'email', 'senha',)


class FormCliente(forms.ModelForm):
    nome_completo = forms.CharField(widget=forms.TextInput(attrs={"id": "nome", "class": "form-Control"}))
    data_de_nascimento = forms.DateField(widget=forms.DateInput(attrs={"id": "data", "class": "form-Control", "type": "date"}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={"id": "cpf", "class": "form-Control"}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={"id": "telefone", "class": "form-Control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"id": "email", "class": "form-Control"}))
    senha = forms.CharField(widget=forms.TextInput(attrs={"type": "password", "class": "form-Control"}))

    class Meta:
        model = Cliente
        fields = ('nome_completo', 'data_de_nascimento', 'cpf' , 'telefone' , 'email' , 'senha' )


class FormEndereco(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ('cep', 'logradouro', 'numero', 'referencia', 'nome_bairro', 'nome_cidade', 'sigla')


class FormLogin(Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"id": "email", "class": "form-Control"}))
    senha = forms.CharField(widget=forms.TextInput(attrs={"type": "password", "class": "form-Control"}))


class FormEmpresa(Form): #porque vc poem "Form" Marcelo? ele nem ta usando esse parametro
    razao_social = forms.CharField(widget=forms.TextInput(attrs={"id": "razao_social", "class": "form-Control"}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={"id": "telefone", "class": "form-Control"}))
    cnpj = forms.CharField(widget=forms.TextInput(attrs={"id": "cnpj", "class": "form-Control"}))

    class Meta:
        model = EmpresaReciclagem
