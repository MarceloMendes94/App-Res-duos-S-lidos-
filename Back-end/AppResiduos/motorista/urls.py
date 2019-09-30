from django.urls import path
from . import views
urlpatterns = [
    path('motorista/' , views.motorista_crud, name='motorista_crud'),
    path('motorista/cadastro/' , views.novo_motorista , name='novo_motorista'),
]