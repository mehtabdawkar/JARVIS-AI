from openai import OpenAI
from Backend.Manager import *
from PIL import Image
from io import BytesIO
import requests

User_Name, User_Assistant_name, User_ApiKey, User_Email, User_Mobile = Read_data_from_database()
client = OpenAI(api_key='')

def GenerateImageUsingOpenAI(query):
    response = client.images.generate(model="dall-e-2",
                                    prompt=query,
      #                                size="256x256",
                                    quality="standard",
                                    n=1)
    image_url = response.data[0].url
    response = requests.get(image_url)
    image_data = response.content
    img = Image.open(BytesIO(image_data))
    img.show()

