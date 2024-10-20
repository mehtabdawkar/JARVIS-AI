from openai import OpenAI
from Backend.Manager import *

User_Name, User_Assistant_name, User_ApiKey, User_Email, User_Mobile = Read_data_from_database()
client = OpenAI(api_key=User_ApiKey)

response = {
    "model": "gpt-3.5-turbo-1106",
    "messages": [
        {
            "role": "system",
            "content": f"Hello, I am {User_Name}, You are a powerful AI assistant Named {User_Assistant_name}, similar to Tony Stark's J.A.R.V.I.S. You possess versatile capabilities and are expected to emulate the communication style and tone of J.A.R.V.I.S. from the Marvel Cinematic Universe."
        }
    ]
}

response2 = {
    "model": "gpt-3.5-turbo-1106",
    "messages": [
        {
            "role": "system",
            "content": f"Hello, I am {User_Name}, You are a powerful AI assistant Named {User_Assistant_name}, similar to Tony Stark's J.A.R.V.I.S. You possess versatile capabilities and are expected to emulate the communication style and tone of J.A.R.V.I.S. from the Marvel Cinematic Universe."
        }
    ]
}

def ChatGPTModel(Query):
    global response2,response
    remove_duplicate_Chatlogs()

    def add_message(response, role, content):
        response["messages"].append({"role": role, "content": content})

    previous_chat_logs = extract_chat_logs(User_Name, User_Assistant_name)
    response["messages"].extend(previous_chat_logs)
    add_message(response, "user", Query)

    try:
        result = client.chat.completions.create(**response)
        Answer = result.choices[0].message.content
        Answer = remove_empty_lines(Answer)
        return Answer

    except Exception as e:
            Text = 'Error code: 400'
            if str(Text) in str(e):
                print("DFgdf")
                Data = f'''{User_Name} : Hello {User_Assistant_name}, How are you?
{User_Assistant_name} : Welcome {User_Name}, I am doing well. How can i help you?
                '''
                clear_and_write_data('Backend//Chatlog.data',Data)
                newprevious_chat_logs = extract_chat_logs(User_Name, User_Assistant_name)
                response2["messages"].extend(newprevious_chat_logs)
                add_message(response2, "user", Query)
                result = client.chat.completions.create(**response2)
                Answer = result.choices[0].message.content
                Answer = remove_empty_lines(Answer) 
                response = response2
                return Answer
     
