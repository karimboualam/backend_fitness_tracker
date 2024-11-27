# Ajout un ViewSet pour les données de progression
# Le ViewSet est une classe qui gère automatiquement les opérations CRUD (Create, Read, Update, Delete) pour un modèle donné.
from django.shortcuts import render
from rest_framework import viewsets
from .models import Progress
from .serializers import ProgressSerializer

# Create your views here.

from .models import Progress
from .serializers import ProgressSerializer

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()   # Retourne tous les enregistrements de la table Progress
    serializer_class = ProgressSerializer  # Utilise le serializer ProgressSerializer

