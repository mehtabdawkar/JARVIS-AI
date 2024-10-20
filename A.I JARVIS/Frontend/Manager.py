
def Read_data_from_database():
    file_path = 'Backend//Data.data'  
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n')
    name = None
    assistant_name = None
    api_key = None
    email = None
    contact_number = None
    for line in data:
        key, value = line.split(' - ')
        if key == 'Name':
            name = value
        elif key == 'Assistant':
            assistant_name = value
        elif key == 'API KEY':
            api_key = value
        elif key == 'Email':
            email = value
        elif key == 'Contact Number':
            contact_number = value
    return name,assistant_name,api_key,email,contact_number

def Update_data_of_database(User_Name, User_Assistant_name, User_ApiKey, User_Email, User_Mobile):
    file_path = 'Backend//Data.data'   
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()

    new_name = str(User_Name)
    new_assistant_name = str(User_Assistant_name)
    new_api_key = str(User_ApiKey)
    new_email = str(User_Email)
    new_contact_number = str(User_Mobile)

    if len(new_name)>0:
        for i, line in enumerate(data):
            if 'Name' in line:
                data[i] = f"Name - {new_name}\n"
    
    if len(new_assistant_name)>0:
        for i, line in enumerate(data):
            if 'Assistant' in line:
                data[i] = f"Assistant - {new_assistant_name}\n"

    if len(new_api_key)>0:
        for i, line in enumerate(data):
            if 'API KEY' in line:
                data[i] = f"API KEY - {new_api_key}\n"

    if len(new_email)>0:
        for i, line in enumerate(data):
            if 'Email' in line:
                data[i] = f"Email - {new_email}\n"
    
    if len(new_contact_number)>0:
        for i, line in enumerate(data):
            if 'Contact Number' in line:
                data[i] = f"Contact Number - {new_contact_number}\n"

    with open(file_path, 'w') as file:
        file.writelines(data)

def database_manager():
    Structure_of_data = '''Name - username
Assistant - Jarvis
API KEY - sk-proj-l9SYpydEKHt8KEkmL5ndT3BlbkFJvOtUrurp5oegpvflblF8
Email - patilMehtab0109@GMAIL.com
Contact Number - +919923453504
'''
    file_path = 'Backend//Data.data'  
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        file.close()
    if len(str(data))>0:
        pass

    else:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(Structure_of_data)
            file.close()  

def show_chat_log_on_gui():
    File = open("Backend//Database.data","r", encoding='utf-8')
    Data = File.read()
    if len(str(Data))>0:
        lines = Data.split('\n')
        lines = lines[:-1]
        result = '\n'.join(lines)
        File.close()
        File = open("Backend//Response.data","w", encoding='utf-8')
        File.write(result)
        File.close()

    else:
        pass

def database_updater_after_saving_the_data_from_gui(User_Name,User_Assistant_name):
    file_path = 'Backend//Database.data'  
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        file.close()
    old_user_Name, old_user_Assistant_name,a,b,c = Read_data_from_database()
    new_data = str(data).replace(old_user_Name,User_Name)
    new_data = str(new_data).replace(old_user_Assistant_name,User_Assistant_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_data)
        file.close()

def chat_log_updater_after_saving_the_data_from_gui(User_Name,User_Assistant_name):
    file_path = 'Backend//ChatLog.data'  
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        file.close()
    old_user_Name, old_user_Assistant_name,a,b,c = Read_data_from_database()
    new_data = str(data).replace(old_user_Name,User_Name)
    new_data = str(new_data).replace(old_user_Assistant_name,User_Assistant_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_data)
        file.close()

def database_setup_if_none_is_history(User_Name, User_Assistant_name):
    file_path = 'Backend//Database.data'  
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    if len(str(data)) > 0:
        pass
    else:
        default_message_to_show_on_gui = f'''{User_Name} : Hello {User_Assistant_name}, How are you?
{User_Assistant_name} : Welcome {User_Name}, I am doing well. How may I assist you?
'''
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(default_message_to_show_on_gui)

def chatlog_setup_if_none_is_history(User_Name, User_Assistant_name):
    file_path = 'Backend//ChatLog.data'  
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    if len(str(data)) > 0:
        pass
    else:
        default_message_to_show_on_gui = f'''{User_Name} : Hello {User_Assistant_name}, How are you?
{User_Assistant_name} : Welcome {User_Name}, I am doing well. How may I assist you?
'''
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(default_message_to_show_on_gui)

