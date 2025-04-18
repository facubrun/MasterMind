import re

import pyttsx3
import speech_recognition as sr

def identify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)[0]
        except IndexError:
            pass
    return name


def initialize_engine():
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.setProperty("voice", "spanish")

    return engine


def recognize_voice(r):
    with sr.Microphone() as source:
        print("Puedes hablar")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es-UY")
    return text

def main():
    engine = initialize_engine()

    engine.say("Hola, como te llamas?")
    engine.runAndWait()

    r = sr.Recognizer()
    text = recognize_voice(r)
    name = identify_name(text)
    if name:
        engine.say("Encantada de conocerte, {}".format(name))
    else:
        engine.say("Me podrias repetir tu nombre?")

    engine.runAndWait()


if __name__ == "__main__":
    main()