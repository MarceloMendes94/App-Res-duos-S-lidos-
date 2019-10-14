from . import views
from django.urls import path

urlpatterns = [
    path('', views.principal, name='principal'),
    path('cliente/', views.cliente, name='cliente'),
    path('motorista/', views.motorista, name='motorista')
]
