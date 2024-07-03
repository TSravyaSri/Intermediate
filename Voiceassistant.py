import speech_recognition as sr
import pyttsx3
import datetime
# Initialize the recognizer
recognizer = sr.Recognizer()
# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
# Function to recognize speech input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"User: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't get that. Could you please repeat?")
            return listen()
        except sr.RequestError:
            speak("Sorry, I am unable to process your request at the moment.")
            return None
# Function to perform actions based on user input
def process_query(query):
    if 'what is your name' in query:
        speak("I am your voice assistant.")
    elif 'hello' in query:
        speak("Hello! How can I help you?")
    elif 'time' in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
    elif 'date' in query:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {current_date}.")
    elif 'thank you' in query:
        speak("You're welcome!")
    elif 'exit' in query:
        speak("Goodbye!")
        return False
    else:
        speak("Sorry, I don't understand that command.")
    return True
# Main function to run the voice assistant
def run_voice_assistant():
    speak("Initializing voice assistant...")
    speak("Hello! How can I assist you?")
    while True:
        query = listen()
        if query:
            if not process_query(query):
                break
if __name__ == "__main__":
    run_voice_assistant()
