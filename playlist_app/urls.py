from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import DetailView, ListView
from django.contrib.auth import views as auth_views
from django.urls import path, include
from playlist_app.views import song_create, song_detail
from .views import index
from playlist_app.models import song

app_name = "playlist_app"

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
    url(r'^$', index),
    path('songs/',
         ListView.as_view(queryset=song,
                          context_object_name='songs_list',
                          template_name='playlist_app/songs.html'),
         name='songs_list'),
    path('songs/create', song_create.as_view(), name='song_create'),

    path('', include('social_django.urls', namespace='social')),

    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

]
