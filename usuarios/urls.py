from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registrar/', views.registrar_usuarios, name='registrar'),
    path('usuarios/', views.lista_usuarios, name='usuarios')
]