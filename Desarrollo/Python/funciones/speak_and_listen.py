import pyttsx3
import speech_recognition as sr
from speech_recognition import UnknownValueError

engine = pyttsx3.init()
engine.setProperty("rate", 200)
engine.setProperty("voice", "spanish")

r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def hear_me():
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language = "es-UY")
            print("He entendido {}".format(text))
        except UnknownValueError:
            print("Lo siento pero no te he escuchado")
    return text

if __name__ == "__main__":
    speak("Probando si funciona todo")
    print(hear_me())