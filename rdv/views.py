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