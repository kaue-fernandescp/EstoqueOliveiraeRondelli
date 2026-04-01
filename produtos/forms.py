from django import forms
from .models import Produtos, Unidades

# Formulário para adicionar um novo produto
class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['pro_referencia',
                  'pro_descricao',
                  'pro_unidade']
        label = {'Referência': '',
                 'Descrição': '',
                 'Unidade': ''}

# Formulário para adicionar uma nova unidade
class UnidadesForm(forms.ModelForm):
    class Meta:
        model = Unidades
        fields = ['uni_nome',
                  'uni_sigla']
        label = {'Nome': '',
                 'Sigla': ''}