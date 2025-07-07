from django.contrib import admin
from django.urls import path, include

urlpatterns = [
     path('admin/', admin.site.urls),
     # tes vues
     path('', include('rdv.urls')),           # les vues Django pour login/logout/password…
     path('', include('django.contrib.auth.urls')),
]