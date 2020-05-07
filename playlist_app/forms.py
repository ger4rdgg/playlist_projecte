from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *
from .models import list
from django.forms import ModelForm


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
            "name": "Nom de la llista",
            "length": "Llargada de la llista"
        }

    def save(self, commit):
        # song = settings.GLOBAL_SETTINGS.get('SONGS_AVAILABLE')
        result = super(song_form, self).save(commit=False)


class ListForm(ModelForm):
    class Meta:
        model = list
        fields = ('name', 'songs',)
