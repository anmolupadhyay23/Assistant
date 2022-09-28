import pyttsx3
import speech_recognition as sr
import os

engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=None,phrase_time_limit=None)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__=='__main__':
    while(True):
        query=takeCommand().lower()
        if "wake up" in query:
            speak("Wait a moment it may take a while")
            os.startfile('D:\\Aqua\\re_aqua.py')
        elif 'exit' in query:
            exit()