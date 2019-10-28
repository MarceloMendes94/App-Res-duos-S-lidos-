from django.contrib import admin
from django.urls import path
from Aplicacao import views
urlpatterns = [
    path('admin/' , admin.site.urls),
    path(''       , views.index),
    path('login/' , views.login_page),
    path('login/submit', views.login_submit),
    path('logout/', views.logout_user),
    path('cadastro/cliente/', views.cliente_cadastro),
    path('perfil/cliente/', views.cliente_perfil),
]
