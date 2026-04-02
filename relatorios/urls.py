from django.urls import path
from . import views

urlpatterns = [
    path('relatorios/', views.relatorios, name='relatorios'),                                           # Adiciona o caminha para a tela seleção de relatórios
    path('relatorio_estoque', views.relatorio_estoque, name='relatorio_estoque'),                       # Adiciona o caminho para a tela do relatório do estoque
    path('relatorio_movimentacoes', views.relatorio_movimentacoes, name='relatorio_movimentacoes')     # Adiciona o caminho para a tela do relatório das movimentações
]