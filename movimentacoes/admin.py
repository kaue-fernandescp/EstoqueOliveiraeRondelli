from django.contrib import admin
from movimentacoes.models import Movimentacao

# Adiciona a tabela Movimentacao na página do Administrador
admin.site.register(Movimentacao)