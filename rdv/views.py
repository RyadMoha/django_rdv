from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import RendezVous

def accueil(request):
    """
    Affiche la page d'accueil en rendant le template 'accueil.html'.
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
            return redirect('login')  # après inscription, on redirige vers la page de connexion
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

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
