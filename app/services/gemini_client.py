import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

def generate_text(prompt : str):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set")
    
    client = genai.Client(api_key = api_key)

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )

    return response.text