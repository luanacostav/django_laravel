from rest_framework import serializers
from .models import Usuario, Chamado, Anexo
from django.contrib.auth.hashers import make_password

class UsuarioSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)

  class Meta:
    model = Usuario
    fields = [
      "id", 
      "nome", 
      "email", 
      "telefone", 
      "departamento", 
      "cargo",
      "password"
    ]
  
  def validate_email(self, value):
    if Usuario.objects.filter(email=value).exists():
      raise serializers.ValidationError("Este e-mail já está em uso.")
    return value

  def create(self, validate_data):
    validate_data['password'] = make_password(validate_data['password'])
    return super().create(validate_data)
  
  def update(self, instance, validate_data):
    if 'password' in validate_data:
      validate_data['password'] = make_password(validate_data['password'])
      return super().update(instance, validate_data)


class ChamadoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Chamado
    fields = [
      "titulo",
      "descricao",
      "data",
      "status",
      "categoria",
      "prioridade",
      "usuario",
    ]

class AnexoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Anexo
    fields = [
      "nome_do_arquivo",
      "caminho_do_arquivo",
      "id_chamado"
    ]