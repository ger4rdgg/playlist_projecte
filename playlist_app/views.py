from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from playlist_app.models import song, list
from django.contrib.auth import logout
from .forms import ListForm

def index(request):
	return render(request, 'index.html', {})

def index1(request):
    context = {
        'songs': song.objects.order_by('-date')
        if request.user.is_authenticated else []
    }

    return render(request, 'playlist_app/index.html', context,
                  {'nsongs': song.objects.count()})

def playlist_list(request):
    playlist = list.objects.order_by('-created_on')
    context= {
        'list' : playlist
    }
    return render(request, 'playlists.html', context)

def playlist_update(request, pk=None):
    llista = get_object_or_404(list, pk=pk)

    if request.method == "POST":
        form = ListForm(request.POST, instance=llista)
        if form.is_valid():
            llista = form.save(commit=False)
            llista.save()
            return redirect('playlist_list')
    else:
        form = ListForm(instance=llista)
    return render(request, 'list_form.html', {"form": form})

def list_detail(request, pk=None):
    llista = list.objects.get(pk=pk)

    context = {
        'llista': llista,

    }
    return render(request, 'list_detail.html', context)

def playlist_remove(request, pk=None):
    llista = get_object_or_404(playlist_list, pk=pk)

    if request.method == "POST":
        llista.delete()
        return redirect('playlist_list')
    context = {
        "llista": llista
    }
    return render(request, "playlist_delete.html", context)

