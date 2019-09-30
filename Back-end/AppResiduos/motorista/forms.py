from django import forms
from .models import Motorista

class PostForm(forms.ModelForm):

    class Meta:
        model = Motorista
        fields = ('nome','cpf','placa','habilitacao','dt_nascimento')
