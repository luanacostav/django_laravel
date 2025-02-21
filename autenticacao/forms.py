from django import forms
from api.models import Usuario

class UsuarioForm(forms.ModelForm):
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

    widgets = {
      'username': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'telefone': forms.TextInput(attrs={'class': 'form-control'}),
      'departamento': forms.TextInput(attrs={'class': 'form-control'}),
      'cargo': forms.TextInput(attrs={'class': 'form-control'}),
      'password': forms.PasswordInput(attrs={'class': 'form-control'})
    }

    labels = {
      'nome': 'Nome Completo',
      'email': 'E-mail',
      'telefone': 'Telefone',
      'departamento': 'Departamento',
      'cargo': 'Crago',
      'password': 'Senha',
    }