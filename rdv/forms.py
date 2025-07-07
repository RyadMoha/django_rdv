# rdv/forms.py
from django import forms
from .models import RendezVous


class RendezVousForm(forms.ModelForm):
    # le choix sera injecté dans la vue (form.fields['heure'].choices = …)
    heure = forms.ChoiceField(choices=[])

    class Meta:
        model = RendezVous
        # le modèle que nous avons créé contient : date, heure, description, utilisateur
        # pas de champ "client", donc on garde ceux‑ci :
        fields = ['date', 'heure', 'description']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 2}),
        }
