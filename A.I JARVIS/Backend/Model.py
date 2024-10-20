from openai import OpenAI
from .Manager import *

User_Name, User_Assistant_name, User_ApiKey, User_Email, User_Mobile = Read_data_from_database()
client = OpenAI(api_key=User_ApiKey)

def AutonomousAI(Query):
        
        response = {
            "model": "gpt-3.5-turbo-1106",
            "messages": [
                {
                    "role": "system",
                "content": "Respond 'True' if the question pertains to time-sensitive information or specific individuals like 'What is today's headline?', 'Who is akshay kumar?', 'Who is India's current prime minister?', 'What's the day today?', 'Tell me something new about YouTube', or queries about individuals like 'Who is Elon' and add the question after 'True' But if the question is asking something that happened before 2021, respond with 'False'. If the question says to any app like 'can you open (appname) for me', respond with 'open (appname)'.If the question says play music or play (songname), respond with 'play (musicname)'. If the questions asks about time, date, day etc. respond with 'time', 'date', 'day' . If the questions ask you to generate or create a image with a specific topic, respond with 'generate image and whatever the topic is'. If the questions is asking for more information but not mentioning the noun like 'tell me more about him' or 'who is he', respond with 'perplex'. If the question ask to search a specific topic on google, Respond with 'google search (topic). 'Otherwise, respond with 'False'."
                }
            ]
        }

        def add_message(response, role, content):
            response["messages"].append({"role": role, "content": content})

        add_message(response, "user", "Who is elon musk?")
        add_message(response, "assistant", "True Who is elon musk?")

        add_message(response, "user", "tell me more about him")
        add_message(response, "assistant", "perplex")
        
        add_message(response, "user", "Explain the concept of calculus.")
        add_message(response, "assistant", "False")

        add_message(response, "user", "Who is the CEO of Tesla?")
        add_message(response, "assistant", "True Who is the CEO of Tesla?")

        add_message(response, "user", "what's his networth?")
        add_message(response, "assistant", "perplex")

        add_message(response, "user", "what is elon musk's current networth?")
        add_message(response, "assistant", "True what is elon musk's current networth?")

        add_message(response, "user", "do you know what is photosynthesis?")
        add_message(response, "assistant", "False")

        add_message(response, "user", "can you explain it?")
        add_message(response, "assistant", "perplex")

        add_message(response, "user", "talk to me, i am bored.")
        add_message(response, "assistant", "False")

        add_message(response, "user", "can you generate a image showing a supra mk4 standing in a rain")
        add_message(response, "assistant", "generate image of a supra mk4 standing in rain")

        add_message(response, "user", "who was maharana pratap?")
        add_message(response, "assistant", "False")

        add_message(response, "user", "search python programming on google")
        add_message(response, "assistant", "google search python programming")

        add_message(response, "user", "Who was the first president of usa?")
        add_message(response, "assistant", "False")

        add_message(response, "user", "can you play how to wear a tie on youtube?")
        add_message(response, "assistant", "play how to wear a tie")

        add_message(response, "user", "can you open facebook for me?")
        add_message(response, "assistant", "open facebook")

        add_message(response, "user", "can you tell me what's the time?")
        add_message(response, "assistant", "time")

        add_message(response, "user", "what's the date today?")
        add_message(response, "assistant", "date")

        add_message(response, "user", "what's the day?")
        add_message(response, "assistant", "day")

        add_message(response, "user", "thanks")
        add_message(response, "assistant", "false")

        add_message(response, "user", "write a python code for creating a snake game")
        add_message(response, "assistant", "False")

        add_message(response, "user", "can you tell me about the recent news related to to sun?")
        add_message(response, "assistant", "True recent news related to to sun")

        add_message(response, "user", Query)

        result = client.chat.completions.create(**response)
        Answer = result.choices[0].message.content
        return Answer
