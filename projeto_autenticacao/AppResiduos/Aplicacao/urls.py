from django.urls import path
from . import views

urlpatterns = [
    path(''                 , views.principal       , name = 'principal' ),
    path('login/'           ,views.login            , name=  'login'),
    path('cadastro/cliente/', views.cadastro_cliente, name = 'cadastro_clientes'),
]