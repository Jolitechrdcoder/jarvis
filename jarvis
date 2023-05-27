import speech_recognition as sr
import subprocess as sub
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyautogui
import keyboard
import os
import serial  # Importa la biblioteca pyserial

escuchar = sr.Recognizer()
inicializar = pyttsx3.init()
velocidad_de_voz = 130
inicializar.setProperty('rate', velocidad_de_voz)
nombre = 'jarvis'

# Configura la comunicación con el Arduino
arduino = serial.Serial('COM6', 9600)  # Reemplazar 'COM6' por el puerto en el que este su arduino o dispositivo

def talk(texto):
    inicializar.say(texto)
    inicializar.runAndWait()

def tomar():
    try:
        with sr.Microphone() as voz:
            print(" Te escucho...")
            talk(" te escucho...")

            voice = escuchar.listen(voz)
            rec = escuchar.recognize_google(voice, language="es")
            rec = rec.lower()
            if nombre in rec:
                rec = rec.replace(nombre, '')
                print(rec)
    except:
        pass
    return rec

def encender_bombillo():
    arduino.write(b'1')  # Envía '1' al Arduino para encender el bombillo

def apagar_bombillo():
    arduino.write(b'0')  # Envía '0' al Arduino para apagar el bombillo

def run_jarvis():
    while True:
        rec = tomar()
        if 'reproduce' in rec:
            musica = rec.replace('reproduce', '')
            talk("OKEY señor")
            pywhatkit.playonyt(musica)
        elif 'hora' in rec:
            time = datetime.datetime.now().strftime('%H:%M')
            print(time)
            talk("Son las " + time)
        elif 'enciende bombillo' in rec:
            encender_bombillo()  # Llama a la función para encender el bombillo
            talk("listo")
        elif 'apaga bombillo' in rec:
            apagar_bombillo()  # Llama a la función para apagar el bombillo
            talk("listo")
        elif 'hasta luego' in rec:
            talk("Hasta luego. Cerrando el programa.")
            arduino.close()  # Cierra la comunicación con el Arduino
            os._exit(0)  # Termina el programa de manera abrupta

while True:
    run_jarvis()
