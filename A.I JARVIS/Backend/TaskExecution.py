from datetime import date,datetime
from pywhatkit import playonyt, search  
import random
from Backend.GoogleSearch import GoogleSearchSystem
import pyautogui
from time import sleep
import webbrowser

professional_responses = [
    "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with.",
    "I'm at your service for any additional questions or support you may need—don't hesitate to ask.",
    "Continued support is my commitment to you. Let me know if there's anything more I can do for you.",
    "I'm here to ensure your experience is seamless. If you have any further requests, please let me know.",
    "Your needs are important to me. If there's anything I can assist you with, I'm just a message away.",
    "I'm dedicated to providing excellent service. Should you require further assistance, I'm here for you.",
    "Exceeding your expectations is my goal. Don't hesitate to reach out for any additional help you may need.",
    "Your satisfaction matters. If you have more questions or need assistance, feel free to ask.",
    "I'm committed to making your experience positive. Let me know if there's anything else I can do for you.",
    "Your feedback is valued. If there's anything I can do to enhance your experience, please let me know.",
    "If there's anything specific you'd like assistance with, please share, and I'll be happy to help.",
    "Your concerns are important to me. Feel free to ask for further guidance or information.",
    "I'm here to address any additional queries or provide clarification as needed.",
    "For a seamless experience, let me know if there's anything else you require assistance with.",
    "Your satisfaction is key; if there's a specific area you'd like more support in, I'm here for you.",
    "Don't hesitate to let me know if there's a particular aspect you'd like further clarification on.",
    "I aim to make your interaction effortless. If there's more you need, feel free to inform me.",
    "Your input is valuable. Please share any additional requirements, and I'll respond promptly.",
    "Should you require more details or have additional questions, I'm ready to provide assistance.",
    "Your success is important to me. If there's anything else you need support with, feel free to ask."]

def get_current_date():
    return date.today()

def get_current_day():
    return datetime.now().strftime("%A")

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

def Play(Topic):
    playonyt(Topic)
    return random.choice(professional_responses)

def Search(Topic):
    search(Topic)
    Answer = GoogleSearchSystem(Topic)
    if "None" == str(Answer):
        return random.choice(professional_responses)

    else:
        return Answer

def OpenApplications(Command):
        sleep(1)
        Appname = Command.lower().replace("open ","").replace(".","").replace(" ","")

        if "youtube" in Appname or "instagram" in Appname or "google" in Appname or "amazon" in Appname or "facebook" in Appname:
            link  = f"https://www.{Appname}.com"
            webbrowser.open(link)
            return random.choice(professional_responses)

        else:

            def open_spotlight_and_search(query):
                sleep(2)  
                pyautogui.hotkey('win')
                sleep(2)  
                pyautogui.write(query)
                sleep(2)  
                pyautogui.press('enter')

            finalnamememe = Command.replace("open ","").lower()
            open_spotlight_and_search(finalnamememe)

        return random.choice(professional_responses)

