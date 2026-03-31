from django.urls import path
from movimentacoes import views

urlpatterns = [
    path('movimentacoes/', views.lista_movimentacoes, name='movimentacoes'),
    path('nova_movimentacao/', views.nova_movimentacao, name='nova_movimentacao'),
]