
def Read_data_from_database():
    file_path = 'Backend//Data.data'  
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n')
    user_name = "Mehtab Dawkar"
    assistant_name = "J.A.R.V.I.S"
    api_key = ""
    email = "dawkarm@gmail.com"
    contact_number = "9326262170"
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

def extract_chat_logs_final(User_Name, User_Assistant_name):
    file_path = 'Backend//Chatlog.data'
    chat_logs = []

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith(f"{User_Name}"):
                chat_logs.append(line)
            elif line.startswith(f"{User_Assistant_name}"):
                chat_logs.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(chat_logs)

def extract_chat_logs(User_Name, User_Assistant_name):
    extract_chat_logs_final(User_Name, User_Assistant_name)
    file_path = 'Backend//Chatlog.data'
    chat_logs = []

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for i in range(0, len(lines), 2):
            user_chat = lines[i].strip()
            assistant_chat = lines[i + 1].strip()
            chat_logs.append({"role": "user", "content": user_chat})
            chat_logs.append({"role": "assistant", "content": assistant_chat})

        if len(lines) % 2 != 0:
            user_chat = lines[-1].strip()
            chat_logs.append({"role": "user", "content": user_chat})

    return chat_logs

def remove_empty_lines(paragraph):
    lines = paragraph.split('\n')
    non_empty_lines = [line for line in lines if line.strip() != '']
    if non_empty_lines:
        updated_paragraph = '\n'.join(non_empty_lines)
        return updated_paragraph
    return paragraph

def clear_and_write_data(file_path, new_data):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_data)

def Chatlog(User_Name, User_Assistant_name,UserChat,AssistantChat):
    File  = open("Backend//Chatlog.data","a", encoding='utf-8')
    CompleteMessage = f'''{User_Name} : {UserChat}
{User_Assistant_name} : {AssistantChat}\n'''
    File.write(CompleteMessage)
    File.close()

def remove_duplicate_Chatlogs():
    try:
        with open('Backend//Chatlog.data', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        modified_lines = [lines[0]]
        for i in range(1, len(lines)):
            current_line_first_word = lines[i].split()[0]
            previous_line_first_word = modified_lines[-1].split()[0]
            if current_line_first_word != previous_line_first_word:
                modified_lines.append(lines[i])

        if len(modified_lines) % 2 == 1:
            modified_lines = modified_lines[:-1]
        with open('Backend//Chatlog.data', 'w', encoding='utf-8') as file:
            file.writelines(modified_lines)

    except:
        pass

def remove_duplicate_database_Chatlog():
    try:
        with open('Backend//Database.data', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        modified_lines = [lines[0]]
        for i in range(1, len(lines)):
            current_line_first_word = lines[i].split()[0]
            previous_line_first_word = modified_lines[-1].split()[0]
            if current_line_first_word != previous_line_first_word:
                modified_lines.append(lines[i])

        if len(modified_lines) % 2 == 1:
            modified_lines = modified_lines[:-1]
        with open('Backend//Database.data', 'w', encoding='utf-8') as file:
            file.writelines(modified_lines)

    except:
        pass

def GetValue(filename):
    try:
        with open(filename,"r", encoding='utf-8') as f:
            value = eval(str(f.read()))
            return value
    except SyntaxError:
        return GetValue(filename)
    except Exception as e:
        return False
    
def SetValue(filename,value):
    with open(filename,"w", encoding='utf-8') as f:
        f.write(str(value))
    with open(filename,"w", encoding='utf-8') as f:
        f.write(str(value))
    return True

def DataBaseChatlog(User_Name, User_Assistant_name,UserChat,AssistantChat):
    File  = open("Backend/Database.data","a", encoding='utf-8')
    CompleteMessage = f'''{User_Name} : {UserChat}
{User_Assistant_name} : {AssistantChat}\n'''
    CompleteMessage = CompleteMessage.replace('\u202f', '')
    File.write(CompleteMessage)
    File.close()

def Query_modifier(query):
    new_query = query.lower().strip()
    query_words = new_query.split()
    
    question_words = ["how", "what", "who", "where", "when", "why", "which", "whose", "whom"]
    if any(word + " " in new_query for word in question_words):
        if query_words[-1][-1] in ['.', '?', '!']:
            new_query = new_query[:-1] + "?"
        else:
            new_query += "?"

    else:
        if query_words[-1][-1] in ['.', '?', '!']:
            new_query = new_query[:-1] + "."
        else:
            new_query += "."

    return new_query.capitalize()

def RealTimeChatLogUpdater(Model,Data):
    Message = f"{Model} : {Data}"
    with open("Backend//Response.data", "w", encoding='utf-8') as file:
        file.write(Message)

