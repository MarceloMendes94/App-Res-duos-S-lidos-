from django import forms
from django.forms import Form

from .models import Motorista
from .models import Cliente
from .models import Endereco


class FormMotorista(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ('habilitacao', 'placa', 'email', 'senha',)


class FormCliente(Form):
    nome_completo = forms.CharField(widget=forms.TextInput(attrs={"id": "nome", "class": "form-Control"}))
    data_de_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={"id": "data", "class": "form-Control", "type": "date"}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={"id": "cpf", "class": "form-Control"}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={"id": "telefone", "class": "form-Control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"id": "email", "class": "form-Control"}))
    senha = forms.CharField(widget=forms.TextInput(attrs={"type": "password", "class": "form-Control"}))

    class Meta:
        model = Cliente


class FormEndereco(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ('cep', 'logradouro', 'numero', 'referencia', 'nome_bairro', 'nome_cidade', 'sigla')


class FormLogin(Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"id": "email", "class": "form-Control"}))
    senha = forms.CharField(widget=forms.TextInput(attrs={"type": "password", "class": "form-Control"}))