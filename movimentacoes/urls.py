from django.urls import path
from movimentacoes import views

urlpatterns = [
    path('movimentacoes/', views.movimentacoes, name='movimentacoes'),      # Caminho para a lista das movimentações
    path('nova_entrada/', views.nova_entrada, name='nova_entrada'),         # Caminho para adicionar uma nova entrada
    path('nova_saida/', views.nova_saida, name='nova_saida'),               # Caminho para adicionar uma nova saída
]