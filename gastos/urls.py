from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
  
    path('adicionar-gasto', views.AdicionarGasto, name='add-gasto'),
    path('editar/<int:id>', views.EditarGasto, name='editar-gasto'),
    path('deletar/<int:id>', views.DeletarGasto, name='deletar-gasto')
]
