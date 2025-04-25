import os
import webbrowser
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file (if you want to store API key there)
load_dotenv()

# Set Gemini API Key
genai.configure(api_key="AIzaSyD5fpkAyZfzLfs6XRpDWE_5OUpWVWbtBjM")


recognizer = sr.Recognizer()
speaker = pyttsx3.init()


# Load Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

def ask_gemini(question):
    try:
        response = model.generate_content(question)
        return response.text.strip()
    except Exception as e:
        print("Error talking to Gemini:", e)
        return "Sorry, I couldn't connect to Gemini."

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "play song" in c:
        webbrowser.open("https://open.spotify.com/playlist/0jdRlG5RrR2j1aCQG9WACQ")
    elif "open insta" in c:
        webbrowser.open("https://instagram.com")
    elif "open today news" in c:
        webbrowser.open("https://indianexpress.com/")
    elif "play my favourite song" in c:
        webbrowser.open("https://youtu.be/0KozfDYK1EU?si=Yu0-aeNAdVD6XXPR")
    elif "exit" in c or "quit" in c or "stop" in c:
        speak("Goodbye Mukund!")
        exit()
    else:
        reply = ask_gemini(c)
        print("Gemini:", reply)
        speak(reply)

if __name__ == "__main__":
    speak("Hello Mukund, how are you? How can I help you?")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word 'Jarvis'...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)

                if word.lower() == "jarvis":
                    speak("Yes?")
                    print("Activated... Listening for command.")
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source, duration=0.5)
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        print("You said:", command)
                        processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")
