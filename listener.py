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
        with s_r.Microphone() as source:
            audio_text = r.listen(source)
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