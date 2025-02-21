from typing import Any
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpRequest

User = get_user_model()

class EmailBackend(BaseBackend):
  def authenticate(self, request, email="", password="", **kwargs):
    print('Sendo usado')
    try:
      user = User.objects.get(email=email.strip().lower())
      print('Usuário encontrado')
      if user.check_password(password):
        return user
    except User.DoesNotExist:
      return None
  
  def get_user(self, user_id):
    try:
      return User.objects.get(pk=user_id)
    except User.DoesNotExist:
      return None