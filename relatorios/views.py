from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from produtos.models import *
from movimentacoes.models import *
from movimentacoes.filters import FiltroMovimentacao

# Função que retorna uma tela para selecionar os relatórios apenas se o usuário estiver logado
@login_required
def relatorios(request):
    return render(request, 'relatorios/menu_relatorios.html')

# Função que retorna o relatório completo do estoque
@login_required
def relatorio_estoque(request):
    produtos = Produtos.objects.all().order_by('pro_descricao')
    context = {'produtos': produtos}
    return render(request, 'relatorios/relatorio_estoque.html', context)

# Função que retorna o relatório das movimentações
def relatorio_movimentacoes(request):
    movimentacoes = Movimentacao.objects.order_by('-mov_data_adicionada')
    filtro = FiltroMovimentacao(request.GET, queryset=movimentacoes)
    context = {'movimentacoes': filtro.qs,
               'filtro': filtro}
    return render(request, 'relatorios/relatorio_movimentacoes.html', context)