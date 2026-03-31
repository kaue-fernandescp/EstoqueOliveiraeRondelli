import django_filters
from django import forms
from .models import Movimentacao
from produtos.models import Produtos

# Classe para realizar a filtragem para as movimentações
class FiltroMovimentacao(django_filters.FilterSet):
    
    # Filtro por produto
    produto = django_filters.ModelChoiceFilter(field_name='mov_produto', queryset=Produtos.objects.all(), label='Produto:')

    # Filtro por intervalo de datas
    data_inicial = django_filters.DateFilter(field_name='mov_data_adicionada', lookup_expr='gte', label='De:', widget=forms.DateInput(attrs={'type': 'date'}))
    data_final = django_filters.DateFilter(field_name='mov_data_adicionada', lookup_expr='lte', label='Até:', widget=forms.DateInput(attrs={'type': 'date'}))

    # Metadados para o filtro
    class Meta:
        model = Movimentacao
        fields = ['produto', 'data_inicial', 'data_final']