from rest_framework import generics

from .models import Usuario, Chamado, Anexo
from .serializers import UsuarioSerializer, ChamadoSerializer, AnexoSerializer


class UsuarioListCreate(generics.ListCreateAPIView):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer

class UsuarioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer
  lookup_field = "pk"


class ChamadoListCreate(generics.ListCreateAPIView):
  queryset = Chamado.objects.all()
  serializer_class = ChamadoSerializer

class ChamadoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Chamado.objects.all()
  serializer_class = ChamadoSerializer
  lookup_field = "pk"

class AnexoListCreate(generics.ListCreateAPIView):
  queryset = Anexo.objects.all()
  serializer_class = AnexoSerializer

class AnexoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Anexo.objects.all()
  serializer_class = AnexoSerializer
  lookup_field = "pk"