import os
import tempfile
import time
import webbrowser

import pygame
import requests 
import speech_recognition as sr
from gtts import gTTS

from client import ask_ai
from musicLib import play

# Initialize pygame mixer for audio playback
pygame.mixer.init()

r = sr.Recognizer()
r.pause_threshold = 0.6
r.energy_threshold = 300


def speak(text):
    """Speak text using Google Text-to-Speech with pygame audio playback"""
    try:
        print(f"[Jarvis]: {text}")

        # Create temporary file for audio
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as tmp:
            tmp_path = tmp.name

        try:
            # Generate speech using gTTS
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(tmp_path)

            # Play using pygame (silent, no window popup)
            pygame.mixer.music.load(tmp_path)
            pygame.mixer.music.play()

            # Wait for audio to finish playing
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

        finally:
            # Clean up temp file
            try:
                os.remove(tmp_path)
            except:
                pass

    except Exception as e:
        print(f"Error speaking: {e}")


def processCommand(command):
    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "play" in command:
        song = command.replace("play", "").strip()
        if play(song):
            speak(f"Playing {song}")
        else:
            speak("I couldn't find that song")

    elif "news" in command:
        speak("Fetching news headlines")
        try:
            # Using a free news API that doesn't require authentication
            url = "https://newsapi.org/v2/top-headlines?country=us&apiKey="
            print("Fetching news...")
            response = requests.get(url, timeout=8)

            if response.status_code == 200:
                data = response.json()
                articles = data.get("articles", [])[:2]

                if articles:
                    for article in articles:
                        title = article.get("title", "").replace(" - ", ". ")
                        if title:
                            print(f"Speaking: {title}")
                            speak(title)
                            time.sleep(0.5)
                else:
                    speak("No news articles available")
            else:
                speak("Unable to fetch news at the moment")

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            speak("Could not connect to the news service")

    else:
        response = ask_ai(command)
        print("AI:", response)
        speak(response)


# -------- START --------

speak("Initializing Jarvis")

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=0.5)

while True:
    try:
        with sr.Microphone() as source:
            print("Listening for wake word...")
            audio = r.listen(source, timeout=2, phrase_time_limit=1)

        word = r.recognize_google(audio, language="en-IN").lower()
        print("Wake word:", word)

        if "jarvis" in word:
            speak("Yes sir")
            time.sleep(0.5)  # Small delay to let speaker finish

            while True:
                try:
                    with sr.Microphone() as source:
                        print("Jarvis Active...")
                        audio = r.listen(
                            source,
                            timeout=3,
                            phrase_time_limit=4
                        )

                    command = r.recognize_google(audio, language="en-IN")
                    print("Command:", command)

                    if "exit" in command.lower() or "sleep" in command.lower():
                        speak("Going to sleep")
                        break

                    processCommand(command)

                except sr.UnknownValueError:
                    speak("Please say that again")

                except sr.WaitTimeoutError:
                    speak("I'm listening")

    except sr.UnknownValueError:
        continue
    except sr.WaitTimeoutError:
        continue
    except KeyboardInterrupt:
        speak("Goodbye")
        break
