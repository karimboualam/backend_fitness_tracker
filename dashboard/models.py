from django.db import models
from django.contrib.auth.models import User

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    metric = models.CharField(max_length=100)  # Exemple: "poids", "distance", "temps"
    value = models.FloatField()  # Valeur mesurée (ex: 70 kg)

    def __str__(self):
        return f"{self.user.username} - {self.metric}: {self.value} ({self.date})"
