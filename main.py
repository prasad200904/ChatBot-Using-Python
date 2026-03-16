from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

SYSTEM_MESSAGE = {
    "role": "system",
    "content": "You are a helpful AI chatbot. Give simple and clear answers."
}

def get_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file")
    return Groq(api_key=api_key)

def get_ai_response(messages):
    client = get_client()
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )
    return response.choices[0].message.content