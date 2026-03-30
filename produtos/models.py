from django.db import models

class Unidades(models.Model):                                                                       # Tabela de Unidades
    uni_nome = models.CharField('Nome', max_length=10)                                              # Nome da unidade
    uni_sigla = models.CharField('Sigla', max_length=5)                                             # Sigla da unidade
    uni_data_adicionada = models.DateTimeField(auto_now_add=True)                                   # Data que foi incluído
    uni_data_modificado = models.DateTimeField(auto_now=True)

    def __str__(self):                                                                              # Função para retornar o nome da unidade
        return self.uni_nome

    class Meta:                                                                                     # Meta dados da unidade
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'
        ordering = ['-uni_nome']

class Produtos(models.Model):                                                                       # Tabela de Produtos
    pro_referencia = models.CharField('Referência', max_length=20, default='SEM-REF')               # Referência do produto
    pro_descricao = models.TextField('Descrição')                                       # Descrição do produto
    pro_unidade = models.ForeignKey(Unidades, on_delete=models.PROTECT, verbose_name='Unidade', default=1)     # Unidade do produto
    pro_preco = models.DecimalField('Preço', decimal_places=2, max_digits=8, default=0)             # Preço do produto
    pro_saldo = models.IntegerField('Saldo', default=0)
    pro_data_adicionada = models.DateTimeField(auto_now_add=True)                                   # Data que foi incluído
    pro_data_modificado = models.DateTimeField(auto_now=True)

    def __str__(self):                                                                              # Função para retornar o nome do produto
        return self.pro_descricao

    class Meta:                                                                                     # Meta dados do produto                                        
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['-pro_descricao']