import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

#configuracion voz
recognizer = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id)  # voz en spanol


#nombre asistente

nombre_asistente = "jarvis"

# almacenamos nuestro name
archivo_nombre ="nombre_usuario.txt"
 

def obtener_nombre_usuario():
    try:
        with open(archivo_nombre , 'r') as file:
            nombre = file.read()
            
            
            
            if nombre:
                
                return nombre
    except FileNotFoundError:
        
        pass
    
    return None        


def establecer_nombre_usuario():
    hablar("Hola , soy jarvis. ¿Cual es tu nombre?")
    
    with sr.Microphone() as source:
        #ajustamos el rtuido ambiental
        recognizer.adjust_for_ambient_noise(source,duration=1)
        
        try:
            audio = recognizer.listen(source,timeout=5,phrase_time_limit=5)
            
            nombre= recognizer.recognize_google(audio,language='es')
            
            with open(archivo_nombre ,'w') as file:
                
             file.write(nombre)
             
            return nombre.lower()  
        
        except sr.WaitTimeoutError:
            return ""
        
        except sr.UnknownValueError:
            return ""
        
        
def obtener_hora_actual():
     hora = datetime.datetime.now()
     
     hora = hora.strftime('%H:%M:%S')
     
     return hora 
 
def obtener_saludo():
    
    hora = datetime.datetime.now()
    
    hora = hora.hour  
    
    if 5<= hora < 12:
        return " Buenos Dias"
    elif 12 <= hora <18:
         return " Buenas Tardes"
    else:
         return " Buenas Noches"       
     
def escuchar_comando():
    
    with sr.Microphone () as source:
        print("Te escucho...")   
        recognizer.adjust_for_ambient_noise(source,duration=1)
        
        
        try:
            
            audio = recognizer.listen(source,timeout=5,phrase_time_limit=5)
            
            texto = recognizer.recognize_google(audio,language='es')
            
            return texto.lower()
        
    
       
        except sr.WaitTimeoutError:
            return ""
        
        except sr.UnknownValueError:
            return ""



def hablar(texto):
    engine.say(texto)
    engine.runAndWait()
nombre_usuario = obtener_nombre_usuario()

if nombre_usuario:
    
    saludo = obtener_saludo()
    hora_actual = obtener_hora_actual()
    
    hablar(f"{saludo},{nombre_usuario.capitalize()}!Son las{hora_actual}.¿ En que puedo servirte? ")            
else:
    nombre_usuario = establecer_nombre_usuario()
    hablar(f"Mucho gusto, {nombre_usuario.capitalize()}.")        

while True:
    comando = escuchar_comando()
    if nombre_asistente.lower() in comando:
        hablar("Sí, ¿en qué puedo ayudarte?")
        while True:
            comando = escuchar_comando()
            if nombre_asistente.lower() in comando:
                hablar("¿En qué más puedo ayudarte?")
            elif 'dormir' in comando:
                hablar("Durmiendo.....")
                break
            elif 'reproduce' in comando:
                busqueda = comando.replace('reproduce', '')
                hablar("Reproduciendo en YouTube " + busqueda)
                pywhatkit.playonyt(busqueda)
                hablar(f"¿En qué más puedo ayudarte, {nombre_usuario.capitalize()}?")
            elif 'hora' in comando:
                hora_actual = obtener_hora_actual()
                hablar(f"La hora actual es {hora_actual}")
            else:
                hablar("No entendí tu peticion. ¿Puedes repetirlo?")
    else:
        print("jarvis está durmiendo....")