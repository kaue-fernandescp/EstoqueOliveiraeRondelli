from django import forms
from .models import Movimentacao

# Formulário para adicionar uma nova movimentação
class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = [
            'mov_produto',
            'mov_tipo',
            'mov_quantidade'
        ]
        label = {
            'Produto': '',
            'Tipo de Movimentação': '',
            'Quantidade': ''
        }

    # Retorna um erro caso a quantidade de saída seja superior ao estoque atual
    def clean(self):
        cleaned_data = super().clean()
        produto = cleaned_data.get('mov_produto')
        quantidade = cleaned_data.get('mov_quantidade')
        tipo = cleaned_data.get('mov_tipo')
        if tipo == 'S' and produto and quantidade:
            if produto.pro_saldo < quantidade:
                raise forms.ValidationError(f"Saldo insuficiente! Estoque atual: {produto.pro_saldo}")
        return cleaned_data