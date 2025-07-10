from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime, time
from rdv.forms import RendezVousForm
from rdv.models import RendezVous  # car le modèle est toujours dans l’app `rdv`
from rdv.utils import generer_creneaux

@login_required
def prendre_rdv(request):
    # 1) Déterminer la date choisie
    if request.method == 'POST':
        date_str = request.POST.get('date')
        try:
            date_selectionnee = datetime.strptime(date_str, "%Y-%m-%d").date()
        except (TypeError, ValueError):
            date_selectionnee = datetime.today().date()
    else:
        date_selectionnee = datetime.today().date()

    # 2) Récupérer les créneaux déjà pris pour cette date
    pris = RendezVous.objects.filter(date=date_selectionnee).values_list('heure', flat=True)

    # 3) Générer les créneaux disponibles
    tous = generer_creneaux(start=time(9, 0), end=time(18, 0), interval_minutes=30)
    choix_dispo = [
        (h.strftime("%H:%M"), h.strftime("%H:%M"))
        for h in tous if h not in pris
    ]

    # 4) Construire / valider le formulaire
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        form.fields['heure'].choices = choix_dispo
        if form.is_valid():
            rdv = form.save(commit=False)
            rdv.utilisateur = request.user
            rdv.save()
            return redirect('dashboard')
    else:
        form = RendezVousForm(initial={'date': date_selectionnee})
        form.fields['heure'].choices = choix_dispo

    return render(request, 'rdv/prise_rdv.html', {'form': form})

@login_required
def dashboard(request):
    """
    Affiche le dashboard du client ou du coach selon le rôle de l'utilisateur.
    """
    user = request.user

    if user.is_superuser:
        # Dashboard coach : affiche tous les rendez-vous
        rdvs = RendezVous.objects.all().order_by('date', 'heure')
        return render(request, 'dashboard_coach.html', {'rdvs': rdvs})
    else:
        # Dashboard client : affiche ses propres rendez-vous
        rdvs = RendezVous.objects.filter(utilisateur=user).order_by('date', 'heure')
        return render(request, 'dashboard_client.html', {'rdvs': rdvs})
