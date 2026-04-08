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
        help_texts = {
            'username': 'Obrigatório. Permitido apenas o uso de letras e ponto (.).'
        }

    # Função para personalizar as mensagens no formulário
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = (
            "<ul>"
            "<li>Sua senha não pode ser parecida com suas outras informações pessoais.</li>"
            "<li>Sua senha deve conter pelo menos 8 caracteres.</li>"
            "<li>Sua senha deve conter pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial.</li>"
            "<li>Sua senha deve ser diferente das três senha utilizadas anteriormente.</li>"
            "</ul>"
        )
        self.fields['password2'].help_text = "Repita a senha anterior para verificação."

# Formulário para editar um usuário
class EditarUsuarioForm(forms.ModelForm):
    is_admin = forms.BooleanField(required=False, label="Usuário é Administrador?")
    
    class Meta:
        model = User
        fields = ['username',
                  'is_active']
        labels = {
            'username': 'Usuário',
            'is_active': 'Ativo'
        }

    # Função que já marca a checkbox "is_admin", caso ele já seja administrador
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['is_active'].help_text = ''
        if self.instance and self.instance.pk:
            self.fields['is_admin'].initial = self.instance.is_superuser