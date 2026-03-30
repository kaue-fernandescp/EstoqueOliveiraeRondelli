from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from .forms import UserCreationFormCustomizado

# Realiza o logout do usuário
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# Verifica se o usuário é Admin
def verifica_admin(usuario):
    return usuario.is_superuser

# Realizar o registro de usuários
@user_passes_test(verifica_admin)
def registrar_usuarios(request):
    if request.method != 'POST':                # Formulário em branco
        form = UserCreationFormCustomizado()
    else:                                       # Processa o formulário preenchido
        form = UserCreationFormCustomizado(data=request.POST)
        if form.is_valid():
            novo_usuario = form.save(commit=False)
            if form.cleaned_data.get('is_admin'):
                novo_usuario.is_staff = True
                novo_usuario.is_superuser = True
            novo_usuario.save()
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'usuarios/registrar_usuario.html', context)

# Mostra os usuários
@user_passes_test(verifica_admin)
def lista_usuarios (request):
    usuarios = User.objects.order_by('username')
    context = {'usuarios': usuarios}
    return render(request, 'usuarios/lista_usuarios.html', context)