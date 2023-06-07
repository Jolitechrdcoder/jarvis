import speech_recognition as sr
import subprocess as sub
import pyttsx3
import pywhatkit
import datetime
import pyautogui
import keyboard
import os

escuchar=sr.Recognizer()

inicializar=pyttsx3.init()

velocidad_de_voz = 130
    
inicializar.setProperty('rate',velocidad_de_voz)

nombre='jarvis'

def talk (texto):
 inicializar.say(texto)
 inicializar.runAndWait()

def tomar():
    
    try:
        with sr.Microphone() as voz:
            print(" Te escucho...")
            talk(" te escucho...")
            
            voice = escuchar.listen(voz)
            rec = escuchar.recognize_google(voice,language="es")
            rec = rec.lower()
            if nombre in rec:
                rec = rec.replace(nombre, '')
                print(rec)
    except:
        pass    
    return rec

def run_jarvis():
    rec = tomar()
    if 'reproduce' in rec:
        musica = rec.replace('reproduce', '')
        talk("OKEY señor")
        pywhatkit.playonyt(musica)
    elif 'hora'in rec:

        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk("son las:"+time)    
while True:         
 run_jarvis()
        