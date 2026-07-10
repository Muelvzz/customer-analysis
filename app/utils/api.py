import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

ENV_API_KEY = os.getenv("AI_API_KEY")

def get_api_key():
  if not ENV_API_KEY:
    return st.error("API key is missing. Please set the AI_API_KEY in the .env file.")
    
  return ENV_API_KEY