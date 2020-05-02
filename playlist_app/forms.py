from django.forms import ModelForm
from playlist_app.models import song


class song_form(ModelForm):
    class Meta:
        model = song
        exclude = ('user', 'date',)
