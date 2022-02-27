import wikipedia
import pyttsx3
import spotipy
import configparser
from lyricsgenius import Genius
from PyDictionary import PyDictionary
from spotipy.oauth2 import SpotifyOAuth

dictionary=PyDictionary()

wikipedia.set_lang("en")

class Broadcaster:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices') 
        self.engine.setProperty('rate', 200)
        self.engine.setProperty('voice', voices[0].id) # 0 for male, 1 for female
        self.engine.setProperty('volume',1.0)
        self.player = SpotifyPlayer()

    def stop(self):
        self.engine.stop()
    
    def answer(self, question):
        if question[0] == 'wikipedia':
            search = wikipedia.search(question[1])[0]
            print(search)
            try:
                page = wikipedia.WikipediaPage(title = search)
                self.engine.say(wikipedia.summary(page.title, sentences=1))
            except:
                self.engine.say('disambiguation error')

        elif question[0] == 'spotify_play':
            if question[1].strip() == "":
                self.player.resume()
            else:
                self.player.play_song(question[1])
        elif question[0] == 'spotify_pause':
            self.player.pause()
        elif question[0] == 'spotify_skip':
            self.player.skip()

        elif question[0] == 'lyrics':
            genius = Genius("oaCj62eaMTHV1KnlH_W0OFLxtovOtfH9-A4Q3obU36TE11it7iPQLn9rY3M4nqcU")
            songs = genius.search_songs(question[1])
            url = songs['hits'][0]['result']['url']
            song_lyrics = genius.lyrics(song_url=url)
            self.engine.say(song_lyrics)

        elif question[0] == 'dictionary':
            query = question[1].strip()
            print(query)
            definition = (dictionary.meaning(query))
            self.engine.say(page.summary)

class SpotifyPlayer:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.cfg')
        scope = "user-read-playback-state,user-modify-playback-state,streaming"

        auth = SpotifyOAuth(
                    client_id="2d0aa7b1e8e34e6db2bbcc9e35fd4db5",
                    client_secret="c76ee05912fa42668927c8456d96274b",
                    redirect_uri="http://google.com/",
                    scope=scope)

        token = auth.get_access_token(as_dict=False)
        self.spotify = spotipy.Spotify(auth=token)

    def play_song(self, song_title):
        devices = self.spotify.devices()
        device_id = devices['devices'][0]['id']
        track = self.spotify.search(song_title)['tracks']['items'][0]['uri']
        self.spotify.start_playback(uris=[track], device_id=device_id)
    
    def pause(self):
        self.spotify.pause_playback()

    def resume(self):
        self.spotify.start_playback()

    def skip(self):
        self.spotify.next_track()