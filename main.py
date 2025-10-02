
import pygame
import os
import time
import speech_recognition as sr
import webbrowser
import Library
import Commands   # <-- import your dictionary-based app commands
from speak import speak
from Listen import listen
import subprocess
import Navigation

def ProcessCommand(text):
    words = text.lower().split()

    if len(words) >= 2 and words[0] == "open":
        app = words[1]
        Commands.open_app(app, speak)   # now dictionary powered
    elif "search" in words:
        query = text.lower().replace("search", "").strip()
        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("Please tell me what to search")
    elif "youtube" in words or "search youtube" in text.lower():
        query = text.lower().replace("youtube", "").replace("search", "").strip()
        if query:
            speak(f"Searching YouTube for {query}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        else:
            speak("Please tell me what to search on YouTube")
    elif "play" in words:
        if len(words) > 1:
            key = words[1]
            if key in Library.Library:
                speak(f"we are playing {key}")
                webbrowser.open(Library.Library[key])
            else:
                speak("Not Found in Library")
        else:
            speak("Please say the name after play")
    elif ("go" in words and "to" in words) or ("open" in words and "folder" in words):
        folder = words[-1]  # take last word (e.g., "documents")
        if folder in Navigation.Navigation:
            path = Navigation.Navigation[folder]
            speak(f"Opening {folder}")
            if os.name == "nt":   # Windows
                os.startfile(path)
            elif os.name == "posix":  # Linux / Mac
                subprocess.Popen(["xdg-open", path])
        else:
            speak("Folder not found in my navigation list")

if __name__=="__main__":
    speak("initiating jarvis.......")
    while True:
        text = listen()
        if text.lower() in ["jarvis", "jarv", "jar"]:
            speak("yes")
            speak("give me any command")
            command = listen(timeout=6, phrase_time_limit=10)
            if command:
                ProcessCommand(command)
            else:
                speak("no command received")

                