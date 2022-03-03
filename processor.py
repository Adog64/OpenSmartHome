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
    elif 'date' in words:
        return ['date']
    elif words == 'make it sexy'.split(' '):
        return ['spotify_play', 'careless whisper']
    elif words == 'set the mood'.split(' '):
        return ['spotify_play', "let's get it on"]
    elif 'die' in words:
        return ['exit']
    #use wikipedia
    elif 'who' == words[0] or 'when' == words[0]:
        if words[1] == 'is' or words[1] == 'are'\
        or words[1] == 'were' or words[1] == 'was':
            text = text[len(words[0]) + len(words[1]) + 1:]
        print(text)
        return ['wikipedia', text]
    else: return [""]