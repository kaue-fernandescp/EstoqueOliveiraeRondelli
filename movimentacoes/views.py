from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Movimentacao
from .forms import *
from .filters import FiltroMovimentacao

# Função para retornar as movimentações apenas se o usuário estiver logado
@login_required
def movimentacoes(request):
    return render(request, 'movimentacoes/movimentacoes.html')

# Função para adicionar uma nova entrada apenas se o usuário estiver logado
@login_required
def nova_entrada(request):
    if request.method != 'POST':
        form = EntradaForm()
    else:
        form = EntradaForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.mov_tipo = 'E'
            movimentacao.mov_usuario = request.user
            movimentacao.save()
            return HttpResponseRedirect(reverse('movimentacoes'))
    context = {'form': form}
    return render(request, 'movimentacoes/nova_entrada.html', context)

# Função para adicionar uma nova entrada apenas se o usuário estiver logado
@login_required
def nova_saida(request):
    if request.method != 'POST':
        form = SaidaForm()
    else:
        form = SaidaForm(request.POST)
        if form.is_valid():
            movimentacao = form.save(commit=False)
            movimentacao.mov_tipo = 'S'
            movimentacao.mov_usuario = request.user
            movimentacao.save()
            return HttpResponseRedirect(reverse('movimentacoes'))
    context = {'form': form}
    return render(request, 'movimentacoes/nova_saida.html', context)