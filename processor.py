from datetime import date
from broadcaster import Broadcaster


def process_text(text):
    words = []
    words = text.lower().split(' ')
    if 'define' in words:
        #use dictionary
        return ['dictionary', text[6:]]
    elif 'play' in words:
        return ['spotify_play', text[4:]]
    elif words[0] == 'pause' or words[0] == 'stop':
        return ['spotify_pause']
    elif words[0] == 'skip':
        return ['spotify_skip']
    elif 'sing' in words:
        return ['lyrics', text[4:]]
        
    elif 'date' or 'time' in words:
        return ['date', text[4:]]
        
        #use wikipedia
    if 'who' == words[0] or 'when' == words[0]:
        if words[1] == 'is' or words[1] == 'are'\
        or words[1] == 'were' or words[1] == 'was':
            text = text[len(words[0]) + len(words[1]) + 1:]
        print(text)
        return ['wikipedia', text]
    else: return [""]