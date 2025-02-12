"""
financeiro\models.py
"""
from django.db import models

class Cobranca(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Pago', 'Pago'),
        ('Cancelado', 'Cancelado'),
    ]

    cliente_software = models.ForeignKey(
        'clientes.ClienteSoftware',
        on_delete=models.CASCADE,
        related_name='cobrancas'
    )
    conta_bancaria = models.ForeignKey(
        'clientes.ContaBancaria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cobrancas'
    )
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')

    def __str__(self):
        return f"Cobrança de {self.cliente_software} - {self.descricao}"
