from Frontend.GUI import GraphicalUserInterface
import threading
import speech_recognition as sr
from Backend.MainExecution import MainExecution
import textwrap
import subprocess
from time import sleep
from Backend.Manager import *
import platform
from Backend.Speak import Speak

current_platform = platform.system()

User_Name, User_Assistant_name, User_ApiKey, User_Email, User_Mobile = Read_data_from_database()

def SetValue(Data):
    with open("Backend//Mic.status", "w", encoding='utf-8') as file:
        file.write(Data)

SetValue("False")

def GetValue():
    with open("Backend//Mic.status", "r", encoding='utf-8') as file:
        Status = file.read()
    return Status

def ChangeTheStatus(Value):
    with open("Backend//Status.data", "w", encoding='utf-8') as file:
        file.write(Value)

def ThreadOne(): # Frontend
    GraphicalUserInterface()

def ThreadTwo(): # Backend

    def TextToSpeech(text):
        ChangeTheStatus("Answering...")

        if text==None:
            return
        
        else:
            Speak(text)

    def SpeechRecognition():
        from Backend.Listen import SpeechRecognitionModel
        ChangeTheStatus("Listening...")
        Query = SpeechRecognitionModel()
        return Query_modifier(Query)

    while True:
        Status = GetValue()

        if Status == "True":
            ChangeTheStatus("Processing....")
            Command = SpeechRecognition()

            if "StatusTrue"==Command:
                pass

            elif "None" == Command:
                pass

            else:
                Command = Query_modifier(Command)
                RealTimeChatLogUpdater(User_Name,Command)
                Answer = MainExecution(Query=Command)
                RealTimeChatLogUpdater(User_Assistant_name,Answer)
                Chatlog(User_Name, User_Assistant_name,Command,Answer)
                DataBaseChatlog(User_Name, User_Assistant_name,Command,Answer)
                TextToSpeech(Answer)

        else:
            with open("Backend//Status.data", "r") as file:
                StatusText = file.read()
                if "Available...." in str(StatusText):
                    sleep(0.1)

                else:
                    with open("Backend//Status.data", "w") as file:
                        file.write("Available....")
                        file.close()

if __name__ == "__main__":
    thread2 = threading.Thread(target=ThreadTwo)
    thread2.start()
    ThreadOne()
    thread2.join()

