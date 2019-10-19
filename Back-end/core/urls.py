from . import views
from django.urls import path


urlpatterns = [
    path('', views.principal, name='principal'),
    path('motorista/', views.motorista, name='motorista'),
    path('motorista/cadastro/', views.motorista_cadastro, name='motorista_cadastro'),
    path('cliente/', views.cliente, name='cliente'),
    path('cliente/cadastro/', views.cliente_cadastro, name='cliente_cadastro'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('cliente/perfil/', views.autenticado_cliente, name='perfil_cliente'),
]
