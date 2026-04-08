from django.db import models

# Tabela das Unidades
class Unidades(models.Model):
    
    # Campos da tabela
    uni_nome = models.CharField('Nome', max_length=10)                  # Nome da unidade
    uni_sigla = models.CharField('Sigla', max_length=5)                 # Sigla da unidade
    uni_data_adicionada = models.DateTimeField(auto_now_add=True)       # Data em que a unidade foi adicionada
    uni_data_modificado = models.DateTimeField(auto_now=True)           # Data em que a unidade foi modificada

    # Retorna o nome da unidade
    def __str__(self):
        return self.uni_nome

    # Metadados da tabela
    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'
        ordering = ['uni_nome']

# Tabela dos Produtos
class Produtos(models.Model):
    pro_referencia = models.CharField('Referência', max_length=20, default='SEM-REF')                                                       # Referência do produto
    pro_descricao = models.TextField('Descrição')                                                                                           # Descrição do produto
    pro_unidade = models.ForeignKey(Unidades, on_delete=models.PROTECT, verbose_name='Unidade', default=1)                                  # Chave estrangeira referenciando a unidade da tabela Unidades
    pro_custo_medio = models.DecimalField('Custo Médio', decimal_places=2, max_digits=10, default=0)                         # Custo médio
    pro_saldo = models.DecimalField('Saldo', decimal_places=2, max_digits=10, default=0)                                                    # Saldo do produto no estoque
    pro_data_adicionada = models.DateTimeField(auto_now_add=True)                                                                            # Data em que o produto foi adicionado
    pro_data_modificado = models.DateTimeField(auto_now=True)                                                                               # Data em que o produto foi modificado

    # Retorna a descrição do produto
    def __str__(self):
        return self.pro_descricao
    
    # Função que realiza o cálculo do custo médio
    def custo_medio(self):
        from movimentacoes.models import Movimentacao
        entradas = Movimentacao.objects.filter(mov_produto=self, mov_tipo='E', mov_custo__gt=0)
        
        if not entradas.exists():
            return 0
        
        total_financeiro = 0
        total_quantidade = 0
        
        for movimentacao in entradas:
            total_financeiro += (movimentacao.mov_quantidade * movimentacao.mov_custo)
            total_quantidade += movimentacao.mov_quantidade 

        if total_quantidade > 0:
            return total_financeiro / total_quantidade
        else:
            return 0

    # Metadados da tabela
    class Meta:                                        
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['pro_descricao']