from django import forms
from .models import Produtos, Unidades

class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['pro_referencia',
                  'pro_descricao',
                  'pro_unidade',
                  'pro_preco']
        label = {'Referência': '',
                 'Descrição': '',
                 'Unidade': '',
                 'Preço': ''}
        
class UnidadesForm(forms.ModelForm):
    class Meta:
        model = Unidades
        fields = ['uni_nome',
                  'uni_sigla']
        label = {'Nome': '',
                 'Sigla': ''}