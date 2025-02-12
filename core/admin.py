"""
core\admin.py
"""
from django.contrib import admin
from .models import Log

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'acao', 'modelo', 'instancia_id', 'data_hora')
    list_filter = ('acao', 'modelo', 'data_hora')
    search_fields = ('usuario__nome_usuario', 'modelo', 'instancia_id')