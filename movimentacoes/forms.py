from django import forms
from .models import Movimentacao

# Formulário para adicionar uma nova movimentação (base)
class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = [
            'mov_produto',
            'mov_quantidade'
        ]
        label = {
            'Produto': '',
            'Quantidade': ''
        }

# Fomrulário para a movimentação do tipo entrada
class EntradaForm(MovimentacaoForm):
    class Meta(MovimentacaoForm.Meta):
        fields = MovimentacaoForm.Meta.fields + ['mov_custo']

# Formulário para a movimentação do tipo saída
class SaidaForm(MovimentacaoForm):

    # Retorna um erro caso a quantidade de saída seja superior ao estoque atual
    def clean(self):
        cleaned_data = super().clean()
        produto = cleaned_data.get('mov_produto')
        quantidade = cleaned_data.get('mov_quantidade')
        tipo = cleaned_data.get('mov_tipo')
        if produto and quantidade:
            if produto.pro_saldo < quantidade:
                raise forms.ValidationError(f"Saldo insuficiente! Estoque atual: {produto.pro_saldo}")
        return cleaned_data