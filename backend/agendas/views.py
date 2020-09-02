from django.shortcuts import render

# Create your views here.

from rest_framework import generics 
from .models import Agenda
from .serializers import AgendaSerializer

class ListAgenda(generics.ListCreateAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class DetailAgenda(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
