from django.urls import path
from .views import (
    listar_planetas,
    adicionar_planeta,
    editar_planeta,
    excluir_planeta,
    ver_planeta,
    inserir_planetas,
    )

urlpatterns = [
    path('portfolio_crud/', listar_planetas, name='listar_planetas'),
    path('portfolio_crud/adicionar_planeta', adicionar_planeta, name='adicionar_planeta'),  
    path('portfolio_crud/editar_planeta/<int:id>/', editar_planeta, name='editar_planeta'),
    path('portfolio_crud/excluir_planeta/<int:id>/', excluir_planeta, name='excluir_planeta'),
    path('portfolio_crud/ver_planeta/<int:id>/', ver_planeta, name='ver_planeta'),
    path('portfolio_crud/inserir_planeta', inserir_planetas, name='inserir_planetas'),
]
