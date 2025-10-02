import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

api_key = os.getenv("OPENAI_API_KEY")
print("API Key Loaded:", api_key[:4] + "***") 