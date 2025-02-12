"""
core\models.py
"""
from django.db import models
from django.contrib.auth import get_user_model

class Log(models.Model):
    TIPO_ACAO_CHOICES = [
        ('CREATE', 'Criação'),
        ('UPDATE', 'Atualização'),
        ('DELETE', 'Exclusão'),
    ]

    usuario = models.ForeignKey(
        'clientes.Usuario',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='logs'
    )
    acao = models.CharField(max_length=10, choices=TIPO_ACAO_CHOICES)
    modelo = models.CharField(max_length=255)
    instancia_id = models.PositiveIntegerField()
    detalhes = models.TextField(blank=True, null=True)
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.acao} - {self.modelo} ({self.instancia_id})"