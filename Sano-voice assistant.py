import speech_recognition as sr
import pyttsx3
import webbrowser
import os

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Use speech_recognition with default microphone (sounddevice backend)
r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Network error. Please check your internet.")
        return ""

def execute_command(command):
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open vscode" in command or "open code" in command:
        speak("Opening Visual Studio Code")
        # Change this path to your VS Code installation
        os.startfile(r"C:\Users\Krish\AppData\Local\Programs\Microsoft VS Code\Code.exe")
    elif "play music" in command:
        speak("Opening Music")
        # Change this path to your music folder
        os.startfile(r"C:\Users\Krish\Music")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I don't know how to do that yet.")

# Main loop
speak("Hello, I am Sano, your assistant. How can I help you today?")
while True:
    cmd = listen()
    if cmd:
        execute_command(cmd)


