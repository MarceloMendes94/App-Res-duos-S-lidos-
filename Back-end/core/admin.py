from django.contrib import admin
from .models import Motorista, Endereco, Cliente, EmpresaCupom, Cupom

admin.site.register(Motorista)
admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(EmpresaCupom)
admin.site.register(Cupom)