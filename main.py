import speech_recognition as sr 

def listenCommand():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("listening....")
            listener.pause_threshold = 1
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'uris' in command:
                print(f"You Said: {command}\n")
    except Exception as e:
        print(e)
        print("Couldn't get you. Try again")
        return "None"
    return command

if __name__ == "__main__":
    listenCommand()