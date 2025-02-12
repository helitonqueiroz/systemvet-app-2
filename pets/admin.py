"""
pets\admin.py
"""
from django.contrib import admin
from .models import Pet, TutorPet, Vacina, Consulta

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('nome_pet', 'tipo_pet', 'raca', 'genero', 'cliente_software')
    search_fields = ('nome_pet', 'raca')
    list_filter = ('tipo_pet', 'genero')

@admin.register(TutorPet)
class TutorPetAdmin(admin.ModelAdmin):
    list_display = ('tutor', 'pet', 'data_inicio_tutela', 'data_fim_tutela')
    search_fields = ('tutor__nome_razao_social', 'pet__nome_pet')
    list_filter = ('data_inicio_tutela', 'data_fim_tutela')

@admin.register(Vacina)
class VacinaAdmin(admin.ModelAdmin):
    list_display = ('pet', 'nome_vacina', 'data_aplicacao', 'proxima_dose')
    search_fields = ('pet__nome_pet', 'nome_vacina')
    list_filter = ('data_aplicacao', 'proxima_dose')

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('pet', 'data_consulta', 'veterinario', 'motivo')
    search_fields = ('pet__nome_pet', 'veterinario')
    list_filter = ('data_consulta',)