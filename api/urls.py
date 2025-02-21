from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
  # Usuários
  path('usuarios/', views.UsuarioListCreate.as_view(), name='usuario-create-view'),
  path(
    'usuarios/<int:pk>/', 
    views.UsuarioRetrieveUpdateDestroy.as_view(), 
    name='usuario-detail'
  ),

  # Chamado
  path('chamado/', views.ChamadoListCreate.as_view(), name='chamado-create-view'),
  path(
    'chamado/<int:pk>/', 
    views.ChamadoRetrieveUpdateDestroy.as_view(), 
    name='chamado-detail'
  ),

  # Anexo
  path('anexo/', views.AnexoListCreate.as_view(), name='anexo-create-view'),
  path(
    'anexo/<int:pk>/', 
    views.AnexoRetrieveUpdateDestroy.as_view(), 
    name='anexo-detail'
  ),
]
