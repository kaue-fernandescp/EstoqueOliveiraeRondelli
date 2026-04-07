from django.urls import path
from core.views import *

urlpatterns = [
    path('core/', home, name = 'index'),                                                # Caminho para a página inicial
    path('manual_produtos/', manual_produtos, name='manual_produtos'),                  # Caminho para a página do manual de produtos
    path('manual_movimentacoes/', manual_movimentacoes, name='manual_movimentacoes')    # Caminho para a página do manual de movimentações
]
