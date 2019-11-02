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
    path('cliente/agendamento/',views.agendamento_cadastro),





    path('cadastro/', views.cadastro),
    path('cadastro/motorista/', views.motorista_cadastro),
    path('cadastro/empresa/', views.empresa_cadastro),
    # path('cliente/loja/', views.cliente_loja),
]
