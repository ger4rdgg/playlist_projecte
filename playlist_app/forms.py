from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *

from datetime import date, timedelta, datetime


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Nom d\'usuari'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contrasenya'}))


class song_form(forms.ModelForm):
    class Meta:
        model = song
        fields = (
            "name",
            "length"
        )
        labels = {
            "name": "Nom de la cançó",
            "length": "Llargada de la cançó"
        }

    def save(self, commit):
        #song = settings.GLOBAL_SETTINGS.get('SONGS_AVAILABLE')
        result = super(song_form, self).save(commit=False)
