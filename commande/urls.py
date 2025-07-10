from django.urls import path
from . import views

urlpatterns = [
    path('prendre/', views.prendre_rdv, name='prendre_rdv'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
