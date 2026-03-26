from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Realiza o logout do usuário
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# Realizar o registro de usuários
def registrar_usuarios(request):
    if request.method != 'POST':                # Formulário em branco
        form = UserCreationForm()
    else:                                       # Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            novo_usuario = form.save()
            usuario_autenticado = authenticate(username=novo_usuario.username, password = request.POST['password1'])        # Verificar se existe usuário para ser autenticado
            login(request, usuario_autenticado)
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'usuarios/registrar_usuario.html', context)