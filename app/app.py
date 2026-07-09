import streamlit as st

def run_app():
    try:
        st.set_page_config(
            page_title="Customer Analysis Tool",
            page_icon="📊",
            layout="centered",
            initial_sidebar_state="expanded"
        )

        st.title("Customer Analysis Tool")
        st.markdown("---")
        st.write("Welcome to the Customer Analysis Tool. Use this application to analyze customer data and gain insights.")
        
    except Exception as e:
        st.error(f"An error occurred while loading the application: {e}")

if __name__ == "__main__":
    # This block executes when the file is run directly by Streamlit
    run_app()