import streamlit as st
import pandas as pd

def check_uploaded_file(uploaded_file):
  try:
    uploaded_file.seek(0)
    df = pd.read_csv(uploaded_file, low_memory=False)

    if df.empty:
      st.error("⚠️ The uploaded CSV file contains no data rows. Please upload a populated CSV file.")
      return False

    elif len(df.columns) == 0:
      st.error("⚠️ The uploaded CSV file contains no columns. Please check the file formatting.")
      return False

    else:
      st.session_state["raw_data"] = df
      return True

  except pd.errors.EmptyDataError:
    st.error("⚠️ The uploaded file is empty or has no parsable data.")
    return False
  
  except pd.errors.ParserError as pe:
    st.error(f"❌ CSV Parser Error: The file layout is invalid. Details: {pe}")
    return False
  
  except Exception as e:
    st.error(f"❌ An unexpected error occurred while parsing the file: {e}")
    return False

def home():
  st.title("Customer Analysis Tool")
  st.markdown("---")

  st.markdown("### 📁 Data Ingestion")
  st.write("Upload your customer review file to start generating insights.")

  uploaded_file = st.file_uploader(
    label="Upload customer data CSV",
    type=["csv"],
    help="Upload a comma-separated values (CSV) file containing customer profiles and their unique ID.",
    label_visibility="collapsed"
  )

  if uploaded_file is not None:
    check_file = check_uploaded_file(uploaded_file)

    return check_file