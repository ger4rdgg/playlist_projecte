from django.shortcuts import render
from playlist_app.models import song


def index(request):
    context = {
        'songs': song.objects.order_by('-date')
        if request.user.is_authenticated else []
    }

    return render(request, 'playlist_app/login.html', context,
                  {'nsongs': song.objects.count()})




