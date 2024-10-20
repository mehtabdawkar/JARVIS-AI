from googlesearch import search
from groq import Groq
from dotenv import load_dotenv
from os import environ
from time import time as t
from rich import print
from json import load,dump

def GoogleSearch(query):
    results = list(search(query, advanced=True, num_results=5))
    a=f"The search results for f'{query} 'are : \n[start]\n "
    for i in results:
        a+=f"Title : {i.title}\nDiscription : {i.description}\n\n"
    a+="[end]"
    return a

load_dotenv()

SYSTEM = [
            {
                  "role": "system",
                  "content": "You are a helpful assistant, reply professionally in less tokens as possible."
            }
            
      ]

messages = []

client = Groq(api_key=environ['GROQ_API'])

def call(Query,Print=True):
    global messages,SYSTEM
    
    SYSTEM.append({"role": "system", "content": GoogleSearch(Query)})

    messages.append({"role": "user", "content": Query})
    completion = client.chat.completions.create(
    model="mixtral-8x7b-32768",
    messages=SYSTEM + messages,
    temperature=0.7,
    max_tokens=2048,
    top_p=1,
    stream=True,
    stop=None,
    )
    r=""
    for chunk in completion:
        if chunk.choices[0].delta.content:
                r += chunk.choices[0].delta.content
        if Print:
                print(chunk.choices[0].delta.content or "", end="")
    messages.append({"role": "assistant", "content": r})

    SYSTEM.pop()
    return r

