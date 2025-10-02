from gtts import gTTS
import pyttsx3
import os
engine = pyttsx3.init()
import pygame

def speak(text):
    """TTS using gTTS + pygame"""
    tts = gTTS(text)
    tts.save("temp.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")
if __name__=="__main__":
    speak("hi")