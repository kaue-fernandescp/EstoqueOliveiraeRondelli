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
    pro_referencia = models.CharField('Referência', max_length=20, default='SEM-REF')                           # Referência do produto
    pro_descricao = models.TextField('Descrição')                                                               # Descrição do produto
    pro_unidade = models.ForeignKey(Unidades, on_delete=models.PROTECT, verbose_name='Unidade', default=1)      # Chave estrangeira referenciando a unidade da tabela Unidades
    pro_custo_medio = models.DecimalField('Custo Médio', decimal_places=2, max_digits=10, default=0)            # Custo médio do produto
    pro_saldo = models.DecimalField('Saldo', decimal_places=2, max_digits=10, default=0)                        # Saldo do produto no estoque
    pro_data_adicionada = models.DateTimeField(auto_now_add=True)                                               # Data em que o produto foi adicionado
    pro_data_modificado = models.DateTimeField(auto_now=True)                                                   # Data em que o produto foi modificado

    # Retorna a descrição do produto
    def __str__(self):
        return self.pro_descricao

    # Metadados da tabela
    class Meta:                                        
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['pro_descricao']