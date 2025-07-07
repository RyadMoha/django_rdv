from django.urls import path
from .views import accueil, signup, dashboard
from .views import prendre_rdv

urlpatterns = [
    path('', accueil, name='accueil'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('prendre-rdv/', prendre_rdv, name='prendre_rdv'),
]