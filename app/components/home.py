import streamlit as st

def home():
  try:
    st.title("Customer Analysis Tool")
    st.markdown("---")
    st.write("Welcome to the Customer Analysis Tool. Use this application to analyze customer data and gain insights.")
      
  except Exception as e:
    st.error(f"An error occurred while loading the home page: {e}")