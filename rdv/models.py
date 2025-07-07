from django.db import models
from django.contrib.auth.models import User

class RendezVous(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    heure = models.TimeField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.utilisateur.username} – {self.date} à {self.heure}"
