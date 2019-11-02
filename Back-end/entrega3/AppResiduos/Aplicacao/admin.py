from django.contrib import admin
from .models import Cliente,Carteira,EmpresaCupom,Cupom


admin.site.register(Cliente)
admin.site.register(Carteira)
admin.site.register(EmpresaCupom)
admin.site.register(Cupom)