from django.contrib.auth.decorators import login_required
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
        'list': playlist
    }
    return render(request, 'playlists.html', context)

@login_required
def playlist_create(request):
    # Creamos un formulario vacío
    form = ListForm()
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = ListForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            llista = form.save(commit=False)
            llista.save()
            form.save_m2m()
            return redirect('playlists')  # ToDo: fer que el botó guardar funcioni i es mostri la llargada de la llista

    # else:
    #     form = song_form()
    return render(request, 'list_form.html', {"form": form})


def playlist_update(request, pk=None):

    llista = get_object_or_404(list, pk=pk)

    if request.method == "POST":
        form = ListForm(request.POST, instance=llista)
        if form.is_valid():
            llista = form.save(commit=False)
            llista.save()
            form.save_m2m()
            return redirect('playlists')
    else:
        form = ListForm(instance=llista)
    return render(request, 'list_form.html', {"form": form})

@login_required
def list_detail(request, pk=None):
    llista = list.objects.get(pk=pk)

    context = {
        'llista': llista,

    }
    return render(request, 'list_detail.html', context)


def playlist_remove(request, pk=None):
    llista = get_object_or_404(list, pk=pk)

    if request.method == "POST":
        llista.delete()
        return redirect('playlists')
    context = {
        "llista": llista
    }
    return render(request, "playlist_delete.html", context)

