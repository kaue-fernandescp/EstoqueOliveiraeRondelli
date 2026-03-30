from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationFormCustomizado(UserCreationForm):
    is_admin = forms.BooleanField(required=False, label="Usuário será Administrador?")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields