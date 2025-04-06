import speech_recognition as sr
import pyttsx3

def record_audio(prompt=""):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(prompt)
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    try:
        return r.recognize_google(audio)
    except:
        return "Sorry, I didn’t catch that."

def engine_speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
