"""
clientes\models.py
"""
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class ClienteSoftware(models.Model):
    TIPO_CLIENTE_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]

    tipo_cliente = models.CharField(max_length=2, choices=TIPO_CLIENTE_CHOICES)
    nome_razao_social = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    data_contrato = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome_razao_social

class Tutor(models.Model):
    TIPO_TUTOR_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]

    tipo_tutor = models.CharField(max_length=2, choices=TIPO_TUTOR_CHOICES)
    nome_razao_social = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome_razao_social


class UsuarioManager(BaseUserManager):
    def create_user(self, nome_usuario, senha=None, cliente_software_id=None, **extra_fields):
        if not nome_usuario:
            raise ValueError("O campo 'nome_usuario' é obrigatório.")
        
        # Busca a instância de ClienteSoftware pelo ID
        if cliente_software_id:
            try:
                cliente_software = ClienteSoftware.objects.get(id=cliente_software_id)
            except ClienteSoftware.DoesNotExist:
                raise ValueError(f"ClienteSoftware com ID {cliente_software_id} não encontrado.")
        else:
            cliente_software = None

        user = self.model(
            nome_usuario=nome_usuario,
            cliente_software=cliente_software,
            **extra_fields
        )
        user.set_password(senha)  # Criptografa a senha
        user.save(using=self._db)
        return user

    def create_superuser(self, nome_usuario, senha=None, cliente_software_id=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(nome_usuario, senha, cliente_software_id, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    cliente_software = models.ForeignKey(
        'ClienteSoftware',
        on_delete=models.CASCADE,
        related_name='usuarios',
        blank=True,
        null=True  # Permite que o campo seja nulo
    )
    nome_usuario = models.CharField(max_length=255, unique=True)
    email = models.EmailField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'nome_usuario'
    REQUIRED_FIELDS = []  # Remove 'cliente_software' dos campos obrigatórios

    def __str__(self):
        return self.nome_usuario
    
class Empresa(models.Model):
    REGIME_TRIBUTARIO_CHOICES = [
        ('Simples Nacional', 'Simples Nacional'),
        ('Lucro Presumido', 'Lucro Presumido'),
        ('Lucro Real', 'Lucro Real'),
    ]

    cliente_software = models.OneToOneField(
        ClienteSoftware,
        on_delete=models.CASCADE,
        related_name='empresa'
    )
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True)
    inscricao_estadual = models.CharField(max_length=20)
    inscricao_municipal = models.CharField(max_length=20, blank=True, null=True)
    regime_tributario = models.CharField(max_length=50, choices=REGIME_TRIBUTARIO_CHOICES)
    cnae_principal = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.razao_social


class ContaBancaria(models.Model):
    TIPO_CONTA_CHOICES = [
        ('Conta Corrente', 'Conta Corrente'),
        ('Conta Poupança', 'Conta Poupança'),
    ]

    cliente_software = models.ForeignKey(
        ClienteSoftware,
        on_delete=models.CASCADE,
        related_name='contas_bancarias'
    )
    banco = models.CharField(max_length=255)
    agencia = models.CharField(max_length=20)
    numero_conta = models.CharField(max_length=50)
    tipo_conta = models.CharField(max_length=50, choices=TIPO_CONTA_CHOICES)
    titular = models.CharField(max_length=255)
    cpf_cnpj_titular = models.CharField(max_length=20)

    class Meta:
        unique_together = ('cliente_software', 'numero_conta')

    def __str__(self):
        return f"{self.banco} - {self.numero_conta}"
