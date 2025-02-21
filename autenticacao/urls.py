from django.urls import path
from . import views

app_name = 'autenticacao'

urlpatterns = [
  path('', views.cadastro_views, name='cadastro'),
  path('login/', views.login_views, name='login'),
]