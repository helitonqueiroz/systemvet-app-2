"""
clientes\admin.py
"""
from django.contrib import admin
from .models import ClienteSoftware, Usuario, Empresa, ContaBancaria, Tutor

@admin.register(ClienteSoftware)
class ClienteSoftwareAdmin(admin.ModelAdmin):
    list_display = ('nome_razao_social', 'tipo_cliente', 'cpf_cnpj', 'email')
    search_fields = ('nome_razao_social', 'cpf_cnpj')
    list_filter = ('tipo_cliente',)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome_usuario', 'email', 'cliente_software')
    search_fields = ('nome_usuario', 'email')
    list_filter = ('cliente_software',)

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'inscricao_estadual', 'regime_tributario')
    search_fields = ('razao_social', 'inscricao_estadual')
    list_filter = ('regime_tributario',)

@admin.register(ContaBancaria)
class ContaBancariaAdmin(admin.ModelAdmin):
    list_display = ('banco', 'agencia', 'numero_conta', 'titular', 'cliente_software')
    search_fields = ('numero_conta', 'titular')
    list_filter = ('banco', 'tipo_conta')

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('nome_razao_social', 'tipo_tutor', 'cpf_cnpj', 'email')
    search_fields = ('nome_razao_social', 'cpf_cnpj')
    list_filter = ('tipo_tutor',)