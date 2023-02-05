# Import speech recognition and text to speech library
import speech_recognition as sr
import pyttsx3 as stx

# Initialize engines from the library
r = sr.Recognizer()
engine = stx.init()

try:
    # Repeats until user breaks the program with N (No)
    while True:
        # Open microphone, and listen from it
        with sr.Microphone() as source:
            print("Please Start Speaking on your Microphone Now!")
    
        # Captures the voice in audio
            audio = r.listen(source)

        # Convert speech into text, and print it
            text = r.recognize_google(audio)
            print("Your Speech:")
            print(text)
            engine.say(text)
            engine.runAndWait()

            user_input = input("Do you want to try again? (Y/N): ")
            if user_input == "Y":
                continue
            else:
                break
       
# Prints Exception
except:
    print("Sorry Your Voice could not be recognized. Please Try Again!")