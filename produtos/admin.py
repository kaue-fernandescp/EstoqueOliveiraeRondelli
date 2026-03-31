from django.contrib import admin
from produtos.models import Produtos, Unidades

# Adiciona as tabelas Produtos e Unidades na página do Administrador
admin.site.register(Produtos)
admin.site.register(Unidades)