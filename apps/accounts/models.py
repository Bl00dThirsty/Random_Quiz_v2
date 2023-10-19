from django.db import models
from django import forms
from django.dispatch import receiver
from django.db.models.signals import pre_save
from uuid import uuid4
from django.utils.crypto import get_random_string
from django.forms import PasswordInput
import os

class Candidat(models.Model):

    matricule = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=100)
    forename = models.CharField(max_length=100)
    code = models.CharField(max_length=100, default=True)
    date = models.DateField()
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    actif = models.BooleanField(default=True)


    class Meta: 
        verbose_name = ("Candidat")
        verbose_name_plural = ("Candidats")
    

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise models.ValidationError("Les mots de passe ne correspondent pas.")

            def __str__(self):
                return self.name
                #return f"{self.name} ({self.stock})"
    def save(self, *args, **kwargs):
        if not self.matricule:
            self.matricule = self.generate_unique_matricule()
        super().save(*args, **kwargs)

    def generate_unique_matricule(self):
        matricule_prefix = 'SLM'
        matricule_digits = get_random_string(length=4, allowed_chars='0123456789')
        return matricule_prefix + matricule_digits

@receiver(pre_save, sender=Candidat)
def assigner_matricule(sender, instance, **kwargs):
    if not instance.matricule:
        instance.matricule = generer_matricule()

def generer_matricule():
    return str(uuid4().hex)

