"""
financeiro\admin.py
"""
from django.contrib import admin
from .models import Cobranca

@admin.register(Cobranca)
class CobrancaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data_vencimento', 'status', 'cliente_software')
    search_fields = ('descricao', 'cliente_software__nome_razao_social')
    list_filter = ('status', 'data_vencimento')
