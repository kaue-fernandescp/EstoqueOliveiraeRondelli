from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Produtos, Unidades
from .forms import ProdutosForm, UnidadesForm

# Produtos

# Mostra os produtos
def lista_produtos(request):
    produtos = Produtos.objects.order_by('pro_descricao')
    context = {'produtos': produtos}
    return render(request, 'produtos/lista_produtos.html', context)

# Detalhes de algum produto
def visualiza_produto(request, id):
    produto = Produtos.objects.get(id = id)
    context = {'produto': produto}
    return render(request, 'produtos/produto.html', context)

# Adiciona um produto
def novo_produto(request):                      # Geralmente, um formulário é recebido como método POST
    if request.method != 'POST':                # Dados não informados
        form = ProdutosForm()
    else:                                       # Dados informados
        form = ProdutosForm(request.POST)
        if form.is_valid():                     # Validação do formulário
            form.save()
            return HttpResponseRedirect(reverse('produtos'))
    context = {'form': form}
    return render(request, 'produtos/novo_produto.html', context)

# Editar algum produto
def alterar_produto(request, id):
    produto = Produtos.objects.get(id=id)
    if request.method != 'POST':                    # Formulário do produto já existente
        form = ProdutosForm(instance=produto)
    else:
        form = ProdutosForm(instance=produto, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produto', args=[produto.id]))
    context = {'produto': produto, 'form': form}
    return render(request, 'produtos/alterar_produto.html', context)

# Unidades

# Mostra as unidades
def lista_unidades(request):
    unidades = Unidades.objects.order_by('uni_nome')
    context = {'unidades': unidades}
    return render(request, 'unidades/lista_unidades.html', context)

# Adicionar uma unidade
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