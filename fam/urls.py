from django.contrib import admin
from django.urls import path
from fam.views import welcome, hora, tipeo, segundo_intento
from familiares.views import family_mermbers, lista_family

urlpatterns = [
    path('admin/', admin.site.urls),
    path("welcome/", welcome, name="welcome"),
    path("hora/", hora, name="hora"),
    path("tipeo/", tipeo, name="tipeo"),
    path("creador/", segundo_intento, name="segundo_intento"),
    path("familymembers/", family_mermbers, name="family_mermbers"),
    path("listado-familiar/", lista_family, name="listado_familiar")
    ]
