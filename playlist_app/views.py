from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from playlist_app.models import song, list
from django.contrib.auth import logout
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .api_wrapper import get_track_list
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
    context = {
        'list': playlist
    }
    return render(request, 'playlist_app/playlists.html', context)


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
    return render(request, 'playlist_app/list_form.html', {"form": form})


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
    return render(request, 'playlist_app/list_form.html', {"form": form})


@login_required
def list_detail(request, pk=None):
    llista = list.objects.get(pk=pk)

    context = {
        'llista': llista,

    }
    return render(request, 'playlist_app/list_detail.html', context)


def playlist_remove(request, pk=None):
    llista = get_object_or_404(list, pk=pk)

    if request.method == "POST":
        llista.delete()
        return redirect('playlists')
    context = {
        "llista": llista
    }
    return render(request, "playlist_app/playlist_delete.html", context)

def songs_searcher(request):
    search_query = request.GET.get('q')
    query_filter = request.GET.get('filter')
    
    if not query_filter:
        query_filter = 'track'

    count, items = get_track_list(search_query, query_filter)
    context = {
        'count' : count,
        'items': items,
        'q': search_query,
        'filter' : query_filter
    }
    return render(request, 'playlist_app/songs_searcher.html', context)


@csrf_exempt
def song_create_ajax(request):
    if request.is_ajax():
        model = song
        song_name = request.POST['song_name']
        s = song.objects.create(name=song_name, length=0)
        model.save(s)

        return True

    return False