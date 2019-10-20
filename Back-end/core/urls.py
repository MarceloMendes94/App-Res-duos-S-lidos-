from . import views
from django.urls import path


urlpatterns = [
    path('', views.principal, name='principal'),
    path('login/', views.login, name='login'),
    path('motorista/', views.motorista, name='motorista'),
    path('motorista/cadastro/', views.motorista_cadastro, name='motorista_cadastro'),
    path('cliente/cadastro/', views.cliente_cadastro, name='cliente_cadastro'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('cliente/perfil/', views.cliente_autenticado, name='perfil_cliente'),
    path('cliente/loja/', views.cliente_loja, name='loja'),
    path('empresa/cadastro/', views.empresa_cadastro, name='cadastro_empresa'),
]
