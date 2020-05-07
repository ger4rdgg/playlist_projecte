from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView
from playlist_app.forms import song_form
from playlist_app.models import song
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView


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


@login_required
class song_create(LoginRequiredMixin, CreateView):
    model = song
    template_name = 'playlist_app/song_form.html'
    form_class = song_form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(song_create, self).form_valid(form)


class song_detail(DetailView):
    model = song
    template_name = 'playlist_app/song_detail.html'

    def get_context_data(self, **kwargs):
        context = super(song_detail, self).get_context_data(**kwargs)
        # context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context
