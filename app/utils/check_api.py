import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AI_API_KEY")

def check_api_key():
  if not API_KEY:
    raise ValueError("API key is missing. Please set the AI_API_KEY environment variable.")
  return API_KEY