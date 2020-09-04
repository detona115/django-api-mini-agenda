from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from .models import Agenda
from .serializers import AgendaSerializer
from .permissions import IsAuthorOrReadOnly

class ListAgenda(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class DetailAgenda(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
