"""
URL configuration for EstoqueOliveiraeRondelli project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import index
from produtos import views

urlpatterns = [
    path('admin/', admin.site.urls),                        # Caminho para a página do administrador
    path('', index, name = 'index'),                        # Caminho para a página inicial
    path('produtos/', include('produtos.urls')),            # Incluir urls.py do App Produtos
    path('usuarios', include('usuarios.urls')),             # Incluir urls.py do App Usuários
]