from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from playlist_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('playlists/', views.playlist_list, name='playlists'),
    path('playlists/create/', views.playlist_create, name='playlist_create'),
    path('playlists/<int:pk>/edit/', views.playlist_update, name='list_update'),
    path('playlists/<int:pk>/delete/', views.playlist_remove, name='list_remove'),
    path('playlists/<int:pk>/', views.list_detail, name='list_detail'),
    path('playlists/searcher', views.songs_searcher, name='songs_searcher'),
    path('playlists/song_create_ajax', views.song_create_ajax, name='song_create_ajax'),
]
