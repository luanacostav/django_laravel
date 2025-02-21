from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
  nome = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  telefone = models.CharField(max_length=20)
  departamento = models.CharField(max_length=150)
  cargo = models.CharField(max_length=100)

  USERNAME_FIELD = "email"
  username = None
  REQUIRED_FIELDS = ["username"]

  def __str__(self) -> str:
    return self.nome


class Chamado(models.Model):

  STATUS_CHOICES = [
    ('ABERTO', 'Aberto'),
    ('ANDAMENTO', 'Em Andamento'),
    ('RESOLVIDO', 'Resolvido')
  ]

  PRIORIDADES_CHOICES = [
    ('BAIXA', 'Baixa'),
    ('MEDIA', 'Média'),
    ('ALTA', 'Alta')
  ]

  CATEGORIAS_CHOICES = [
    ('HARDWARE', 'Problema de Hardware'),
    ('SOFTWARE', 'Problema de Software'),
    ('DUVIDA', 'Dúvida'),
    ('OUTROS', 'Outros')
  ]

  titulo = models.CharField(max_length=150)
  descricao = models.TextField()
  data = models.DateField(auto_now_add=True)
  status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='ABERTO')
  categoria = models.CharField(max_length=20, choices=CATEGORIAS_CHOICES)
  prioridade = models.CharField(max_length=10, choices=PRIORIDADES_CHOICES)
  usuario = models.ForeignKey('Usuario', on_delete=models.SET_NULL, null=True)

  def __str__(self) -> str:
    return self.titulo


class Anexo(models.Model):
  nome_do_arquivo = models.CharField(max_length=255)
  caminho_do_arquivo = models.FileField(upload_to='anexos/')
  id_chamado = models.ForeignKey('Chamado', on_delete=models.CASCADE)

  def __str__(self) -> str:
    return self.nome_do_arquivo
