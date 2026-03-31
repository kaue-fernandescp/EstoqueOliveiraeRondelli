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
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),                        # Caminho para a página do administrador
    path('', RedirectView.as_view(url='login/')),                   # Redireciona para a página de login
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('core/', include('core.urls')),                    # Caminho para a página inicial
    path('produtos/', include('produtos.urls')),            # Incluir urls.py do App Produtos
    path('usuarios/', include('usuarios.urls')),             # Incluir urls.py do App Usuários
    path('movimentacoes/', include('movimentacoes.urls')), 
]