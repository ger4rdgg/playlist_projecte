from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from playlist_app.models import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from .forms import song_form, ListForm
from .api_wrapper import get_track_list
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'users/login.html', {})


def welcome(request):
    return render(request, 'users/welcome.html', {})


def index1(request):
    context = {
        'songs': song.objects.order_by('-date')
        if request.user.is_authenticated else []
    }

    return render(request, 'playlist_app/index.html', context,
                  {'nsongs': song.objects.count()})


# @login_required
# class song_create(LoginRequiredMixin, CreateView):
#     model = song
#     template_name = 'playlist_app/list_form.html'
#     form_class = song_form
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(song_create, self).form_valid(form)


# class song_detail(DetailView):
#     model = song
#     template_name = 'playlist_app/list_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(song_detail, self).get_context_data(**kwargs)
#         # context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
#         return context


def playlist_list(request):
    playlist = list.objects.order_by('-created_on')
    context = {
        'list': playlist
    }
    return render(request, 'playlist_app/playlists_list.html', context)


def playlist_create(request):
    # Creamos un formulario vacío
    form = song_form()
    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = song_form(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            llista = form.save(commit=False)
            llista.save()
            form.save_m2m()
            return redirect(
                'playlist_app:playlist_list')  # ToDo: fer que el botó guardar funcioni i es mostri la llargada de la llista

    return render(request, 'playlist_app/playlist_create.html', {"form": form})


# def playlist_length(request, pk=None):
#     llista = get_object_or_404(list, pk=pk)
#
#     if request.method == "POST":
#         form = ListForm(request.POST, instance=llista)
#         if form.is_valid():
#
#


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
        'count': count,
        'items': items,
        'q': search_query,
        'filter': query_filter
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
