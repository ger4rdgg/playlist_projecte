import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

song_uri = 'spotify:track:6kLCHFM39wkFjOuyPGLGeQ'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.track(song_uri)

print(results)
