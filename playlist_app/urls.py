from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import DetailView, ListView
from django.contrib.auth import views as auth_views
from django.urls import path, include
from playlist_app.views import list_detail, playlist_update, playlist_remove
from .views import index
from playlist_app.models import song
from playlist_app import views

app_name = "playlist_app"

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
    url(r'^$', index),
    # path('songs/',
    #      ListView.as_view(queryset=song.objects.all(),
    #                       context_object_name='songs_list',
    #                       template_name='playlist_app/songs.html'),
    #      name='songs_list'),
    # path('songs/create/', song_create, name='song_create'),

#    url('list_details/(?P<id>\d+)/$', list_detail, name='list_detail'),

    path('', include('social_django.urls', namespace='social')),
    path('playlists/<int:pk>/', views.list_detail, name='list_detail'),
    path('playlists/delete/<int:pk>/', views.playlist_remove, name='list_remove'),
    path('playlists/edit/<int:pk>', views.playlist_update, name='list_update'),
    path('playlists/create/', views.playlist_create, name='playlist_create'),
    path('playlists/list', views.playlist_list, name='playlist_list'),

    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

]
