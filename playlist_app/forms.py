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
        model = list
        fields = (
            "name",
            "description"
        )
        labels = {
            "name": "Nom",
            "description": "Descripció"

        }


class ListForm(ModelForm):
    class Meta:
        model = list
        fields = ('name', 'songs',)
