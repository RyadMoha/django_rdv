from django.urls import path
from .views import accueil, signup, dashboard
from commande.views import prendre_rdv
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', accueil, name='accueil'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('prendre-rdv/', prendre_rdv, name='prendre_rdv'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]