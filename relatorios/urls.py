from django.urls import path
from . import views

urlpatterns = [
    path('relatorios/', views.relatorios, name='relatorios'),                                           # Caminho para a página seleção de relatórios
    path('relatorio_estoque', views.relatorio_estoque, name='relatorio_estoque'),                       # Caminho para a página do relatório do estoque
    path('relatorio_movimentacoes', views.relatorio_movimentacoes, name='relatorio_movimentacoes')      # Caminho para a página do relatório das movimentações
]