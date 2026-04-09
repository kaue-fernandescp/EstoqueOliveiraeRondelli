import django_filters
from django import forms
from django.contrib.auth.models import User
from .models import Movimentacao
from produtos.models import Produtos

# Classe para realizar a filtragem para as movimentações
class FiltroMovimentacao(django_filters.FilterSet):
    
    # Filtro por produto
    produto = django_filters.ModelChoiceFilter(field_name='mov_produto', queryset=Produtos.objects.all().order_by('pro_descricao'), label='Produto:')

    # Filtro por tipo de movimentação
    tipo = django_filters.ChoiceFilter(field_name='mov_tipo', choices=Movimentacao.TIPO_MOVIMENTACAO, label='Tipo:')

    # Filtro por usuário
    usuario = django_filters.ModelChoiceFilter(field_name='mov_usuario', queryset=User.objects.all().order_by('username'), label='Usuário:')

    # Filtro por intervalo de datas
    data_inicial = django_filters.DateFilter(field_name='mov_data_adicionada', lookup_expr='gte', label='De:', widget=forms.DateInput(attrs={'type': 'date'}))
    data_final = django_filters.DateFilter(field_name='mov_data_adicionada', lookup_expr='lte', label='Até:', widget=forms.DateInput(attrs={'type': 'date'}))

    # Metadados para o filtro
    class Meta:
        model = Movimentacao
        fields = ['produto', 'tipo', 'usuario', 'data_inicial', 'data_final']