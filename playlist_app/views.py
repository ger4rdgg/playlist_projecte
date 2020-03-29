from django.shortcuts import render
from playlist_app.models import song
from django.contrib.auth import logout

def index(request):
	return render(request, 'index.html', {})

def index1(request):
    context = {
        'songs': song.objects.order_by('-date')
        if request.user.is_authenticated else []
    }

    return render(request, 'playlist_app/index.html', context,
                  {'nsongs': song.objects.count()})




