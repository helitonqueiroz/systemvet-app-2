"""
clientes\views.py
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UsuarioForm  # Formulário personalizado para registro
from core.middleware import get_current_user  # Importa o método para recuperar o usuário

def login_view(request):
    if request.method == 'POST':
        nome_usuario = request.POST['nome_usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=nome_usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após o login
        else:
            messages.error(request, "Nome de usuário ou senha inválidos.")
    
    # Exemplo de uso do middleware
    usuario_atual = get_current_user()
    if usuario_atual:
        print(f"Usuário atual na view: {usuario_atual}")
    else:
        print("Nenhum usuário autenticado.")

    return render(request, 'clientes/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após o logout

def registrar_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Faça login.")
            return redirect('login')
    else:
        form = UsuarioForm()
    
    # Exemplo de uso do middleware
    usuario_atual = get_current_user()
    if usuario_atual:
        print(f"Usuário atual na view: {usuario_atual}")
    else:
        print("Nenhum usuário autenticado.")

    return render(request, 'clientes/registrar.html', {'form': form})