from django.contrib import admin
from .models import Candidat


class Recherche(admin.ModelAdmin):
    search_fields = ['name', 'forename', 'date']  

admin.site.register(Candidat, Recherche)
# Register your models here.
