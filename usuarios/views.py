from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from .forms import *

# Função que realiza o logou do usuário
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# Função que verifica se o usuário é Admin
def verifica_admin(usuario):
    return usuario.is_superuser

# Função que realiza o cadastro de usuários apenas se o usuário for Admin
@user_passes_test(verifica_admin)
def registrar_usuarios(request):
    if request.method != 'POST':                
        form = UserCreationFormCustomizado()
    else:                                       
        form = UserCreationFormCustomizado(data=request.POST)
        if form.is_valid():
            novo_usuario = form.save(commit=False)
            if form.cleaned_data.get('is_admin'):
                novo_usuario.is_staff = True
                novo_usuario.is_superuser = True
            novo_usuario.save()
            return HttpResponseRedirect(reverse('usuarios'))
    context = {'form': form}
    return render(request, 'usuarios/registrar_usuario.html', context)

# Função que retornar os usuários cadastrados apenas se o usuário for Admin
@user_passes_test(verifica_admin)
def lista_usuarios (request):
    usuarios = User.objects.order_by('username')
    context = {'usuarios': usuarios}
    return render(request, 'usuarios/lista_usuarios.html', context)

# Função que permite editar os usuário apenas se o usuário for Admin
@user_passes_test(verifica_admin)
def editar_usuario(request, id):
    usuario = User.objects.get(id=id)
    if request.method != 'POST':                
        form = EditarUsuarioForm(instance=usuario)
    else:                                       
        form = EditarUsuarioForm(instance=usuario, data=request.POST)
        if form.is_valid():
            usuario_admin = form.cleaned_data['is_admin']
            usuario.is_superuser = usuario_admin
            usuario.is_staff = usuario_admin
            form.save()
            return HttpResponseRedirect(reverse('usuarios'))
    context = {'usuario': usuario, 'form': form}
    return render(request, 'usuarios/editar_usuario.html', context)