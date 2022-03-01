import wikipedia
import pyttsx3
import spotipy
import configparser
from lyricsgenius import Genius
from PyDictionary import PyDictionary
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime


dateNow = datetime.now() # current date and time
month = dateNow.strftime("%m")
year = dateNow.strftime("%Y")

dateNow = year
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
        if question[0] == 'date':
            self.engine.say('the month is')
            self.engine.say(month)
            self.engine.say('the year is')
            self.engine.say(year)
            print(dateNow)


        if question[0] == 'wikipedia':
            search = wikipedia.search(question[1])[0]
            print(search)
            try:
                page = wikipedia.WikipediaPage(title = search)
                self.engine.say(wikipedia.summary(page.title, sentences=1))
            except:
                self.engine.say('disambiguation error')
        elif question[0] == 'anthony_play':
            if question[1].strip() == "":
                self.player.resume()
            else:
                self.player.play_song(question[1])
        elif question[0] == 'anthony_pause':
            self.player.pause()
        elif question[0] == 'anthony_skip':
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
                    client_id="f504761a0a624a0f9c36ae9a5ec9deb0",
                    client_secret="97a7e10a0b454540aecf3e7b8044442b",
                    redirect_uri="http://localhost:9000",
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