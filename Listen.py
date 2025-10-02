import speech_recognition as sr

def listen(timeout=10, phrase_time_limit=15):
    """
    Listen to microphone input and return recognized text.
    - timeout: how long to wait before user starts talking
    - phrase_time_limit: max duration for user speech
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Adjust for background noise (important for clarity)
        r.adjust_for_ambient_noise(source, duration=1)
        print("🎤 Listening...")

        try:
            # Capture audio
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

            # Recognize speech
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text

        except sr.WaitTimeoutError:
            print("⏳ No speech detected.")
            return ""
        except sr.UnknownValueError:
            print("🤔 Sorry, I could not understand.")
            return ""
        except sr.RequestError:
            print("⚠️ Could not connect to recognition service.")
            return ""
