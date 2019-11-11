from django.contrib import admin
from django.urls import path
from Aplicacao import views
urlpatterns = [
    path('admin/' , admin.site.urls),
    path(''       , views.index),
    path('login/' , views.login_page),
    path('login/submit', views.login_submit),
    path('logout/', views.logout_user),
    path('cliente/cadastro/', views.cliente_cadastro),
    path('cliente/perfil/', views.cliente_perfil),
    path('cliente/coleta/', views.pedir_coleta),

    path('motorista/cadastro/', views.motorista_cadastro),
    path('motorista/perfil/', views.motorista_perfil),
    path('motorista/coleta/',views.visualizar_coletas),
    path('motorista/coleta/pesagem/',views.pesagem_coleta),

    path('relatorio/pesagem/',views.relatorio_pesagens),
    path('relatorio/cupom/',views.relatorio_cupons),


    path('cadastro/', views.cadastro),
    
    path('empresa/cadastro/', views.empresa_cadastro),
    
]
