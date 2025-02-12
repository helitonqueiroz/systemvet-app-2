"""
pets\models.py
"""
from django.db import models

class Pet(models.Model):
    TIPO_PET_CHOICES = [
        ('Canino', 'Canino'),
        ('Felino', 'Felino'),
        ('Bovino', 'Bovino'),
        ('Equino', 'Equino'),
        ('Aves', 'Aves'),
        ('Silvestres', 'Silvestres'),
        ('Outros', 'Outros'),
    ]
    GENERO_CHOICES = [
        ('Macho', 'Macho'),
        ('Fêmea', 'Fêmea'),
    ]

    cliente_software = models.ForeignKey(
        'clientes.ClienteSoftware',
        on_delete=models.CASCADE,
        related_name='pets'
    )
    nome_pet = models.CharField(max_length=255)
    tipo_pet = models.CharField(max_length=50, choices=TIPO_PET_CHOICES)
    raca = models.CharField(max_length=255)
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)
    peso = models.FloatField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_pet


class TutorPet(models.Model):
    tutor = models.ForeignKey(
        'clientes.Tutor',  # Usa a nova classe Tutor
        on_delete=models.CASCADE,
        related_name='pets_tutor'
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name='tutores'
    )
    data_inicio_tutela = models.DateField()
    data_fim_tutela = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ('tutor', 'pet')

    def __str__(self):
        return f"{self.tutor} - {self.pet}"

class Vacina(models.Model):
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name='vacinas'
    )
    nome_vacina = models.CharField(max_length=255)
    data_aplicacao = models.DateField()
    proxima_dose = models.DateField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome_vacina} - {self.pet}"


class Consulta(models.Model):
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name='consultas'
    )
    data_consulta = models.DateTimeField()
    veterinario = models.CharField(max_length=255)
    motivo = models.TextField()
    diagnostico = models.TextField(blank=True, null=True)
    prescricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Consulta de {self.pet} em {self.data_consulta}"