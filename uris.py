import speech_recognition as sr
import pyttsx3
import datetime 
import webbrowser 
import pywhatkit
import wikipedia  
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    talk('Hello! I am Uris at your service all time. How can i assist you?')

def listen_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            talk('Listening...')
            listener.pause_threshold = 1
            voice = listener.listen(source)
            query = listener.recognize_google(voice)
            query = query.lower()
        if 'uris' in query:
            print(query)
    except Exception as e:
        print('try again') 
    return query

def run_uris():
    command = listen_command()
    print(command)

if __name__ == "__main__":
    greet()
    while True:

        query = listen_command().lower()
        if 'wikipedia' in query:
            talk('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            talk("According to Wikipedia")
            print(results)
            talk(results)

        elif 'play' in query:
            song = query.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in query:
            person = query.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'date' in query:
            talk('sorry, I have a headache')
        elif 'are you single' in query:
            talk('I am in a relationship with wifi')
        elif 'joke' in query:
            talk(pyjokes.get_joke())
        elif 'open google' in query:
                webbrowser.open("google.com")
        else:
            talk('Please say the query again.')
run_uris()
