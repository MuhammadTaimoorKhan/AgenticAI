import os 
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
chat = client.chats.create(
    model="gemini-2.0-flash"
)
def respond(user_query):
    response = chat.send_message(user_query)
    return response.candidates[0].content.parts[0].text


