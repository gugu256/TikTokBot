from gtts import gTTS

def doTTS(text, type: str):
    tts = gTTS(text, )
    tts.save(type + ".mp3")