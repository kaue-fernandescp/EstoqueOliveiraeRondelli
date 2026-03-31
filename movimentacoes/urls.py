from django.urls import path
from movimentacoes import views

urlpatterns = [
    path('movimentacoes/', views.lista_movimentacoes, name='movimentacoes'),            # Caminho para a lista das movimentações
    path('nova_movimentacao/', views.nova_movimentacao, name='nova_movimentacao'),      # Caminho para adicionar uma nova movimentação
]