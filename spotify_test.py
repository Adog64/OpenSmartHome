from spotipy.oauth2 import SpotifyOAuth
import spotipy
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')
scope = "user-read-playback-state,user-modify-playback-state,streaming"

auth = SpotifyOAuth(
            client_id="2d0aa7b1e8e34e6db2bbcc9e35fd4db5",
            client_secret="c76ee05912fa42668927c8456d96274b",
            redirect_uri="http://google.com/",
            scope=scope)

token = auth.get_access_token(as_dict=False)

spotify = spotipy.Spotify(auth=token)

devices = spotify.devices()
device_id = devices['devices'][0]['id']

song_title = 'here comes the sun'

track = spotify.search(song_title)['tracks']['items'][0]['uri']
spotify.start_playback(uris=[track], device_id=device_id)