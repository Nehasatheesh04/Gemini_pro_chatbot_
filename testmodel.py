from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

print("Available models:\n")

for model in client.models.list():  # ✅ Direct iteration
    print("-", model.name)
