from .models import list
from django.forms import ModelForm


class ListForm(ModelForm):

    class Meta:
        model = list
        fields = ('name', 'songs', 'description',)