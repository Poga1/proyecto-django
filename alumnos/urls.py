from django.urls import  path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('Carro', views.Carro, name='Carro'),
    path('Registro', views.Registro, name='Registro'),
    path('Ropa', views.Ropa, name='Ropa'),
    path('Login', views.Login, name='Login'),
    path('contactanos', views.contactanos, name='contactanos'),
]