from django.contrib import admin
from .models import Cliente,Empresa,Motorista,Carteira,EmpresaCupom,Cupom,Residuo,Coleta,Pesagem, TransacaoMensal, ComprovanteEntrega 


admin.site.register(Cliente)
admin.site.register(Empresa)
admin.site.register(Motorista)
admin.site.register(Carteira)
admin.site.register(EmpresaCupom)
admin.site.register(Cupom)
admin.site.register(Residuo)
admin.site.register(Coleta)
admin.site.register(Pesagem)
admin.site.register(ComprovanteEntrega)
admin.site.register(TransacaoMensal)