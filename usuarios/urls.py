from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),     # Caminho para a tela de login
    path('logout/', views.logout_view, name='logout'),                                                   # Caminho para a tela de logout
    path('registrar/', views.registrar_usuarios, name='registrar'),                                      # Caminho para a tela de criação de usuários
    path('usuarios/', views.lista_usuarios, name='usuarios'),                                            # Caminho para a tela de visualização de usuários
    path('usuario/<id>/', views.editar_usuario, name='usuario')                                               # Caminho para a tela de editar usuário
]