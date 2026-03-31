from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Movimentacao
from .forms import MovimentacaoForm

# Função para retornar as movimentações apenas se o usuário estiver logado
@login_required
def lista_movimentacoes(request):
    movimentacoes = Movimentacao.objects.order_by('-mov_data_adicionada')
    context = {'movimentacoes': movimentacoes}
    return render(request, 'movimentacoes/lista_movimentacoes.html', context)

# Função para adicionar uma nova movimentação apenas se o usuário estiver logado
@login_required
def nova_movimentacao(request):
    if request.method != 'POST':
        form = MovimentacaoForm()
    else:
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.mov_usuario = request.user
            movimentacao.save()
            return HttpResponseRedirect(reverse('movimentacoes'))
    context = {'form': form}
    return render(request, 'movimentacoes/nova_movimentacao.html', context)