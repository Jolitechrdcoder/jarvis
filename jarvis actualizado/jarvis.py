import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

# Configuración del reconocimiento de voz
r = sr.Recognizer()

#configuracion voz

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)#Voz en espanol


#activar asistente
def escuchar_palabra_activacion():
    with sr.Microphone() as source:
        print("DI jarvis para activarme....")
        r.adjust_for_ambient_noise(source, duration=1)   # ajusta el ruido de fondo
        audio = r.listen(source)

    try:
        texto = r.recognize_google(audio, language='es')
        if 'jarvis' in texto:
            return True
    except sr.UnknownValueError:
        return False
    
# funcion para escuhar  
def escuchar_comando():
    with sr.Microphone() as source:
        print("Te escucho....")
        r.adjust_for_ambient_noise(source, duration=1)  # ajusta el ruido de fondo
        audio = r.listen(source)

    try:
        texto = r.recognize_google(audio,language='es')
        print("comando detected..." + texto)
        return texto.lower()# convertimos todo a minuscula
    except sr.UnknownValueError:
        return ""
# funcion para darle voz
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

activado = False
# aqui gestionamos los comandos del asistente
while True:
    if not activado:
        if escuchar_palabra_activacion():
            activado = True
            hablar("Sí, ¿en qué puedo ayudarte?")
    else:
        comando = escuchar_comando()
        
        if comando == "":
            hablar("No detecto ningun comando..")
        elif 'apagar' in comando:
            hablar("hasta pronto,   Apagado.....")
            break
        elif 'reproduce' in comando:
            cancion = comando.replace('reproduce', '')
            hablar("Reproduciendo " + cancion)
            pywhatkit.playonyt(cancion)
        elif 'hora' in comando:
            hora_actual = datetime.datetime.now().strftime('%H:%M:%S')
            hablar("La hora actual es: " + hora_actual)
        else:
            hablar("No entendi tu comando.")

