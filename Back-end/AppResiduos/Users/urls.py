from . import views
from django.urls import path

urlpatterns = [
    path('motorista/cadastro/', views.motorista_cadastro, name='motorista_cadastro'),
    path('cliente/cadastro/', views.cliente_cadastro, name='cliente_cadastro')
]
