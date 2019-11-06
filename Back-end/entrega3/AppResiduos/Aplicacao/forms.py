from django import forms
from .models import Cliente, Endereco, Empresa, Motorista
from django.forms import Form
from django.contrib.auth.models import User


class ClienteForm(forms.ModelForm):
    nome_completo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    # https://stackoverflow.com/questions/48654968/create-input-mask-for-use-in-django-forms adicionar jquery mask nos templates
    cpf = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'data-mask': '000.000.000-00'}))
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cliente


class EnderecoForm(Form):
    estado = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    cidade = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    bairro = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    logradouro = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    cep = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'data-mask': '00000-000'}))
    numero = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    referencia = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Endereco


class EmpresaForm(Form):
    razao_social = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    cnpj = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Empresa

# Como coloco/estendo informações como nome, coisas de pessoa?


class MotoristaForm(Form):
    habilitacao = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = Motorista
