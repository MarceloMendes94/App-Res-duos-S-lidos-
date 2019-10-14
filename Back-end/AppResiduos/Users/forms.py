from django import forms
from .models import Motorista
from .models import Cliente
from .models import Endereco


class FormMotorista(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ('habilitacao', 'placa', 'email', 'senha',)


class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('cpf', 'email', 'senha',)



class FormEndereco(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ('cep', 'logradouro','numero', 'referencia','nome_bairro','nome_cidade','sigla')