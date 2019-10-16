from django.contrib import admin
from .models import Motorista
from .models import Endereco
from .models import Cliente


admin.site.register(Motorista)
admin.site.register(Cliente)
admin.site.register(Endereco)