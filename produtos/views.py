from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Produtos, Unidades
from .forms import ProdutosForm, UnidadesForm

# Função para retornar os produtos cadastrados apenas se o usuário estiver logado
@login_required
def lista_produtos(request):
    pesquisa = request.GET.get('search')
    if pesquisa:
        produtos = Produtos.objects.filter(pro_descricao__icontains=pesquisa)
    else:
        produtos = Produtos.objects.order_by('pro_saldo')[:5]
    context = {'produtos': produtos}
    return render(request, 'produtos/lista_produtos.html', context)

# Função para retornar os detalhes de algum produto apenas se o usuário estiver logado
@login_required
def visualiza_produto(request, id):
    produto = Produtos.objects.get(id = id)
    context = {'produto': produto}
    return render(request, 'produtos/produto.html', context)

# Função para adicionar um novo produto apenas se o usuário estiver logado
@login_required
def novo_produto(request):                      
    if request.method != 'POST':                
        form = ProdutosForm()
    else:                                      
        form = ProdutosForm(request.POST)
        if form.is_valid():                    
            form.save()
            return HttpResponseRedirect(reverse('produtos'))
    context = {'form': form}
    return render(request, 'produtos/novo_produto.html', context)

# Função para editar o produto apenas se o usuário estiver logado
@login_required
def alterar_produto(request, id):
    produto = Produtos.objects.get(id=id)
    if request.method != 'POST':                   
        form = ProdutosForm(instance=produto)
    else:
        form = ProdutosForm(instance=produto, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produto', args=[produto.id]))
    context = {'produto': produto, 'form': form}
    return render(request, 'produtos/alterar_produto.html', context)

# Função para retornar as unidades cadastradas apenas se o usuário estiver logado
@login_required
def lista_unidades(request):
    unidades = Unidades.objects.order_by('uni_nome')
    context = {'unidades': unidades}
    return render(request, 'unidades/lista_unidades.html', context)

# Função para adicionar uma nova unidade apenas se o usuário estiver logado
@login_required
def nova_unidade(request):
    if request.method != 'POST':               
        form = UnidadesForm()
    else:                                   
        form = UnidadesForm(request.POST)
        if form.is_valid():                     
            form.save()
            return HttpResponseRedirect(reverse('unidades'))
    context = {'form': form}
    return render(request, 'unidades/nova_unidade.html', context)