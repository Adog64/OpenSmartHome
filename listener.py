import speech_recognition as s_r

# wake anthony
wake_anthony = ['anthony']

# If anthony is called
def look_for_prompt():
    prompted = False
    print('Go')
    while not prompted:
        print('waiting for prompt...')
        audio_text = ""
        text = ""
        r = s_r.Recognizer()
        r.energy_threshold = 500
        with s_r.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=1)
            try:
                audio_text = r.listen(source)
            except:
                pass
        try:
            text = r.recognize_google(audio_text)
        except:
            pass
        text = text.lower()
        text = text.strip()
        print(text)
        for w in text.split(' '):
            if w in wake_anthony:
                prompted = True  
                return text[text.find(w) + len(w):].strip()