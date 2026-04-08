from django.db import models, transaction
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from produtos.models import Produtos

# Tabela das Movimentações
class Movimentacao(models.Model):

    # Tipos de movimentações
    TIPO_MOVIMENTACAO = [
        ('E', 'Entrada'),
        ('S', 'Saída')
    ]

    # Campos da tabela
    mov_produto = models.ForeignKey(Produtos, on_delete=models.PROTECT, related_name='movimentacoes', verbose_name='Produto')   # Chave estrangeira referenciando o produto da tabela Produtos
    mov_usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário')                                     # Chave estrangeira referenciando o usuário da tabela Usuários
    mov_quantidade = models.DecimalField('Quantidade relativa à Unidade de Medida', decimal_places=2, max_digits=10)                                     # Quantidade da movimentação
    mov_tipo = models.CharField('Tipo de Movimentação', max_length=1, choices=TIPO_MOVIMENTACAO)                                # Tipo da movimentação
    mov_saldo_movimento = models.IntegerField('Saldo no momento:', editable=False, null=True)                                   # Saldo do produto após movimentação
    mov_custo = models.DecimalField('Valor da Compra', max_digits=10, decimal_places=2, null=True, blank=True)                   # Preço do produto que está entrando
    mov_data_adicionada = models.DateTimeField(auto_now_add=True)                                                               # Data que foi adicionada

    # Retorna --> Produto - Unidade
    def __str__(self):
        return f"{self.mov_produto} - {self.mov_produto.pro_unidade.uni_sigla}"

    # Realiza cálculo do saldo do estoque
    def save(self, *args, **kwargs):
        with transaction.atomic():
            produto = Produtos.objects.select_for_update().get(pk=self.mov_produto.pk)
            if self.mov_tipo == 'E':
                produto.pro_saldo += self.mov_quantidade
                produto.pro_custo_medio = self.mov_custo / self.mov_quantidade
            else:
                if self.mov_tipo == 'S' and produto.pro_saldo < self.mov_quantidade:
                    raise ValueError('Saldo em estoque insuficiente.')
                else:
                    produto.pro_saldo -= self.mov_quantidade

            produto.save()
            self.mov_saldo_movimento = produto.pro_saldo
            super().save(*args, **kwargs)

    # Metadados da tabela
    class Meta:
        verbose_name = 'Movimentação'
        verbose_name_plural = 'Movimentações'
        ordering = ['-mov_data_adicionada']