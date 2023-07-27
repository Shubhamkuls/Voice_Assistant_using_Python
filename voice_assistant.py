# Creating a voice assistant using Python involves a combination of speech recognition, natural language processing, 
# and text-to-speech conversion. Below, I'll outline the steps to build a basic voice assistant using the speech_recognition,
# pyttsx3, and pyaudio libraries in Python.
import speech_recognition as sr
import pyttsx3

# Step 2: Initialize the speech recognizer and text-to-speech converter
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Step 3: Define functions for speech recognition and text-to-speech

def listen():
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        # Optional: Adjust for background noise
        recognizer.adjust_for_ambient_noise(source)
        # Listen for audio input from the user
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        # Use Google Web Speech API to convert speech to text
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError:
        print("Sorry, I couldn't access the speech recognition service.")
    return ""

def speak(text):
    # Use the text-to-speech engine to convert text to speech and speak
    tts_engine.say(text)
    tts_engine.runAndWait()

# Step 4: Implement the main voice assistant logic

def main():
    speak("Hello! I am your voice assistant. How can I assist you today?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello there!")

        elif "what's your name" in command:
            speak("I am an AI language model. You can call me Assistant.")

        elif "who made you" in command:
            speak("I was created by Shubham.")

        elif "goodbye" in command:
            speak("Goodbye! Have a great day!")
            break

        else:
            speak("I'm sorry, I didn't recognize that command. Please try again.")

# Step 5: Run the voice assistant

if __name__ == "__main__":
    main()