from openai import OpenAI
from Backend.Manager import *

User_Name, User_Assistant_name, User_ApiKey, User_Email, User_Mobile = Read_data_from_database()
client = OpenAI(api_key=User_ApiKey)

def ScrapeChats():
    FileNew = open("Backend//Chatlog.data","r", encoding='utf-8')
    DataNew = FileNew.read()
    FileNew.close()
    Data = DataNew.splitlines()
    DataList = Data[-6:]
    return DataList

def NounDetector(NewList):
    response = {
        "model": "gpt-3.5-turbo-1106",
        "messages": [
            {"role": "system",
             "content": "As an AI model, Your proficiency lies in recognizing and identifying the specific noun or person within our ongoing chatlog, don't return the noun or person who is being discussed before the latest noun or person. You are designed to provide you with only the most accurate information, delivering the precise name associated with the entity currently under discussion and return it."
             }
        ]
    }

    List = ['Kaushik : Hello jarvis how are you?','Jarvis : Good day. I am functioning optimally and ready to assist you.','Kaushik : Can you tell me who is kaushik shreshth?','Jarvis : According To The Google Search, Kaushik Shresth is an online educator.']
    List2 = ['Kaushik : Can you tell me who is kaushik shreshth?','Jarvis : According To The Google Search, Kaushik Shresth is an online educator.','Kaushik : Do you know about illuminati?','Jarvis : Sorry, I cannot assist with that.']

    def add_message(response, role, content):
        response["messages"].append({"role": role, "content": content})
    add_message(response, "user", f"Data : {List}")
    add_message(response, "assistant", "Kaushik Shresth")
    add_message(response, "user", f"Data : {List2}")
    add_message(response, "assistant", "Illuminati")
    add_message(response, "user", f"Data : {NewList}")

    result = client.chat.completions.create(**response)
    Answer = result.choices[0].message.content
    return Answer

def ChangeNounWithPronouns(Sentence,Name):
    response = {
        "model": "gpt-3.5-turbo-1106",
        "messages": [
            {
                "role": "system",
            "content": "As an AI Model, You are designed to replace pronouns in the given sentence with the name which is provided to make the sentence complete. example : 'who is he?' and the name given is 'elon musk', replace 'elon musk' with 'he' and return the complete sentence 'who is elon musk'."
            }
        ]
    }

    def add_message(response, role, content):
        response["messages"].append({"role": role, "content": content})
    add_message(response, "user", f"Sentence : 'tell me more about him', Name : satyam")
    add_message(response, "assistant", "tell me more about satyam")
    add_message(response, "user", f"Sentence : {Sentence}, Name : {Name}")

    result = client.chat.completions.create(**response)
    Answer = result.choices[0].message.content
    return Answer

