from django.contrib import admin
from django.urls import path, include
from produtos import views

urlpatterns = [
    path('produtos/', views.lista_produtos, name='produtos'),                           # Caminho para a página dos produtos
    path('produto/<id>/', views.visualiza_produto, name='produto'),                     # Caminho para a página de um produto específico
    path('novo_produto/', views.novo_produto, name = 'novo_produto'),                   # Caminho para a página de adicionar um novo produto
    path('alterar_produto/<id>/', views.alterar_produto, name = 'alterar_produto'),     # Caminho para a página de editar algum produto
    path('unidades/', views.lista_unidades, name = 'unidades'),                         # Caminho para a página das unidades
    path('nova_unidade/', views.nova_unidade, name = 'nova_unidade')                    # Caminho para a página de adicionar uma nova unidade
]