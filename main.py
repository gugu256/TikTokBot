import grabber
import tts

post = grabber.get_post()
tts.doTTS(post["title"], "title")
tts.doTTS(post["content"], "content")