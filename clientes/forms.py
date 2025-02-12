"""
clientes\forms.py
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('cliente_software', 'nome_usuario', 'password1', 'password2')