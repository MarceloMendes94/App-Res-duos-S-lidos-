from django.contrib import admin
from .models import Cliente,Empresa,Motorista,Carteira,EmpresaCupom,Cupom


admin.site.register(Cliente)
admin.site.register(Empresa)
admin.site.register(Motorista)
admin.site.register(Carteira)
admin.site.register(EmpresaCupom)
admin.site.register(Cupom)