from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RendezVousForm
from .models import RendezVous
from datetime import datetime, timedelta, time, date
from .utils import generer_creneaux


def accueil(request):
    """
    Affiche la page d'accueil en rendant template 'accueil.html'.
    """
    return render(request, 'accueil.html')

def signup(request):
    """
    Inscription d’un nouvel utilisateur via le formulaire Django.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')   # après inscription, on renvoie vers la connexion
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def dashboard(request):
    """
    Affiche le dashboard client ou coach en fonction du rôle.
    """
    user = request.user

    if user.is_superuser:
        # Dashboard du coach : on récupère tous les rendez-vous
        rdvs = RendezVous.objects.all().order_by('date', 'heure')
        return render(request, 'dashboard_coach.html', {'rdvs': rdvs})
    else:
        # Dashboard du client : on filtre ses propres rendez-vous
        rdvs = RendezVous.objects.filter(utilisateur=user).order_by('date', 'heure')
        return render(request, 'dashboard_client.html', {'rdvs': rdvs})

@login_required
def prendre_rdv(request):
    # --- 1) déterminer la date choisie ---
    if request.method == 'POST':
        date_str = request.POST.get('date')
        try:
            date_selectionnee = datetime.strptime(date_str, "%Y-%m-%d").date()
        except (TypeError, ValueError):
            date_selectionnee = datetime.today().date()
    else:
        date_selectionnee = datetime.today().date()

    # --- 2) récupérer les créneaux déjà pris pour cette date ---
    pris = RendezVous.objects.filter(date=date_selectionnee)\
                             .values_list('heure', flat=True)

    # --- 3) générer les créneaux disponibles ---
    tous = generer_creneaux(start=time(9, 0), end=time(18, 0), interval_minutes=30)
    choix_dispo = [
        (h.strftime("%H:%M"), h.strftime("%H:%M"))
        for h in tous if h not in pris
    ]

    # --- 4) construire / valider le formulaire ---
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
