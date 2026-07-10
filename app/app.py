import streamlit as st
from components.home import home
from utils.api import get_api_key

def run_app():
    get_api_key()

    try:
        home()
    except Exception as e:
        st.error(f"An error occurred while loading the application: {e}")

if __name__ == "__main__":
    # This block executes when the file is run directly by Streamlit
    run_app()