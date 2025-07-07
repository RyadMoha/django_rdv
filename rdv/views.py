from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RendezVousForm

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
    # Supposons que le coach est superutilisateur (is_superuser)
    if user.is_superuser:
        # Dashboard du coach : on pourra passer la liste de toutes les séances
        return render(request, 'dashboard_coach.html', {})
    else:
        # Dashboard du client : on pourra filtrer ses propres séances
        return render(request, 'dashboard_client.html', {})

@login_required
def prendre_rdv(request):
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            rdv = form.save(commit=False)
            rdv.utilisateur = request.user
            rdv.save()
            return redirect('dashboard')  # redirige vers la page principale
    else:
        form = RendezVousForm()
    return render(request, 'rdv/prise_rdv.html', {'form': form})