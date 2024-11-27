#Ajout un sérialiseur pour les modèles de progression.
#Les serializers convertissent les objets Django (modèles) en données JSON et vice-versa.
from rest_framework import serializers
from .models import Progress

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__' # Inclut tous les champs du modèle Progress
