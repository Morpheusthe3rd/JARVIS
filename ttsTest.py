from gtts import gTTS
import os
from playsound import playsound

tts = gTTS(text="Hello World", lang="en")
tts.save("hello.mp3")

playsound('hello.mp3')
