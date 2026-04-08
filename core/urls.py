from django.urls import path
from core.views import *

urlpatterns = [
    path('core/', home, name = 'index'),                                                # Caminho para a página inicial
    path('manual_produtos/', manual_produtos, name='manual_produtos'),                  # Caminho para a página do manual de produtos
    path('manual_movimentacoes/', manual_movimentacoes, name='manual_movimentacoes'),   # Caminho para a página do manual de movimentações
    path('manual_relatorios/', manual_relatorios, name='manual_relatorios'),            # Caminho para a página do manual de relatórios
    path('manual_unidades/', manual_unidades, name='manual_unidades'),                  # Caminho para a página do manual de unidades
    path('manual_usuarios/', manual_usuarios, name='manual_usuarios')                   # Caminho para a página do manual de usuários
]