from django.contrib import admin
from .models import Cliente, Endereco, Carteira, Agendamento
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Carteira)
admin.site.register(Endereco)
admin.site.register(Agendamento)