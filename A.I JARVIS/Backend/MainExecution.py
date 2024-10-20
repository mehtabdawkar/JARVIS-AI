from Backend.ChatGPT import *
from Backend.GoogleSearch import *
from Backend.Manager import *
from Backend.Model import *
from Backend.Perplexity import *
from Backend.GoogleSearch import *
from Backend.ImageGeneration import *
from Backend.TaskExecution import *
from Backend.History import *
from pywhatkit import search as GoogleSearch
from random import choice

def ChangeTheStatus(Value):
    with open("Backend//Status.data", "w", encoding='utf-8') as file:
        file.write(Value)

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

def MainExecution(Query):

    ChangeTheStatus("Thinking....")
    Decision = str(AutonomousAI(Query=Query)).lower()
    print(Decision)
    
    if "true" in Decision:
        ChangeTheStatus("Searching....")
        Question = Decision.removeprefix("True").strip()
        Answer = GoogleSearchSystem(query=Question)

        if "None" == str(Answer):
            ChangeTheStatus("Deep Searching....")
            Answer = call(Query=Question)
            if len(str(Answer))>0:
                return Answer
            
            else:
                GoogleSearch(topic=Question)
                return choice(professional_responses)
        
        else:
            return Answer

    elif "generate image" in Decision:
        ChangeTheStatus("Generating....")
        GenerateImageUsingOpenAI(Decision) # type: ignore
        return choice(professional_responses)

    elif "false" in Decision:
        Answer = ChatGPTModel(Query=Query)
        return Answer

    elif "perplex" in Decision:
        Data = ScrapeChats()
        ChangeTheStatus("Processing....")
        Noun = NounDetector(Data)
        ChangeTheStatus("Scraping....")
        Sentence = ChangeNounWithPronouns(Query,Noun)
        ChangeTheStatus("Searching....")
        Answer = call(Query=Sentence)
        if len(str(Answer))>0:
            return Answer
        
        else:
            GoogleSearch(topic=Question)
            return choice(professional_responses)
            
    elif "time" in Decision:
        timenow = get_current_time()
        return f"Current time is {timenow}"

    elif "date" in Decision:
        datetoday = get_current_date()
        return f"Today's date is {datetoday}"

    elif "day" in Decision:
        daytoday = get_current_day()
        return f"Today is {daytoday}"

    elif "play" in Decision:
        Topic = str(Query).lower().replace("play","")
        return Play(Topic=Topic)

    elif "google search" in Decision:
        Topic = str(Query).lower().replace("google search ","")
        return Search(Topic=Topic)

    elif "open" in Decision:
        Answer = OpenApplications(Decision)
        return Answer
    
    else:
        Answer = ChatGPTModel(Query=Query)
        return Answer

