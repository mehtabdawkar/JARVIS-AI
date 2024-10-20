import pyttsx3 # pip install pyttsx3

Assistant = pyttsx3.init('sapi5')
Voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',Voices[0].id)
Assistant.setProperty('rate',180)

def Speak(Audio):
    print(f"Assistant : {Audio}")
    print("  ")
    Assistant.say(Audio)
    Assistant.runAndWait()
    print("  ")

