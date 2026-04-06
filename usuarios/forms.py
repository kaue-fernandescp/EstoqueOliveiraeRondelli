from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Formulário customizado para adicionar um novo usuário
class UserCreationFormCustomizado(UserCreationForm):
    is_admin = forms.BooleanField(required=False, label="Usuário será Administrador?")

    # Metadados para o formulário
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

# Formulário para editar um usuário
class EditarUsuarioForm(forms.ModelForm):
    is_admin = forms.BooleanField(required=False, label="Usuário é Administrador?")
    
    class Meta:
        model = User
        fields = ['username',
                  'is_active']
        labels = {
            'username': 'Usuário',
            'is_active': 'Ativo?'
        }

    # Função que já marca a checkbox "is_admin", caso ele já seja administrador
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['is_admin'].initial = self.instance.is_superuser