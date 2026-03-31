from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Função para renderizar a página index apenas com o usuário logado
@login_required
def index(request):
    return render(request, 'core/index.html')