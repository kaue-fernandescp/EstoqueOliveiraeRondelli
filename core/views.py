from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from produtos.models import Produtos
from movimentacoes.models import Movimentacao
from django.db.models import Sum, F, FloatField

# Função para retornar o dashboard da tela inicial apenas como usuário logado
@login_required
def home(request):
    total_produtos = Produtos.objects.count()

    media = Produtos.objects.aggregate(total=Sum(F('pro_saldo') * F('pro_custo_medio'), output_field=FloatField()))
    total_custo_medio = media['total']

    estoque_critico = Produtos.objects.filter(pro_saldo__lt=5).order_by('pro_saldo')
    ultimas_movimentacoes = Movimentacao.objects.all().order_by('-mov_data_adicionada')[:5]
    context = {
        'total_produtos': total_produtos,
        'total_custo_medio': total_custo_medio,
        'estoque_critico': estoque_critico,
        'ultimas_movimentacoes': ultimas_movimentacoes
    }
    return render(request, 'core/index.html', context)

# Função que renderiza o manual de Produtos apenas se o usuário estiver logado
@login_required
def manual_produtos(request):
    return render(request, 'core/manual_produtos.html')

# Função que renderiza o manual de Movimentações apenas se o usuário estiver logado
@login_required
def manual_movimentacoes(request):
    return render(request, 'core/manual_movimentacoes.html')

# Função que renderiza o manual de Relatórios apenas se o usuário estiver logado
@login_required
def manual_relatorios(request):
    return render(request, 'core/manual_relatorios.html')

# Função que renderiza o manual de Unidades apenas se o usuário estiver logado
@login_required
def manual_unidades(request):
    return render(request, 'core/manual_unidades.html')

# Função que renderiza o manual de Usuários apenas se o usuário estiver logado
@login_required
def manual_usuarios(request):
    return render(request, 'core/manual_usuarios.html')