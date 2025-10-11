import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Streamlit
st.set_page_config(
    page_title="Chat with Gemini 2.5 Pro",
    page_icon="🤖",
    layout="centered",
)

# Get API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("⚠️ GOOGLE_API_KEY not found in .env or secrets.")
    st.stop()

# Configure Google client
genai.configure(api_key=GOOGLE_API_KEY)
MODEL_NAME = "models/gemini-2.5-pro"

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("💬 Gemini 2.5 Pro Chatbot")

# Display previous messages
for role, content in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(content)

# Chat input
user_prompt = st.chat_input("Ask Gemini something...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append(("user", user_prompt))

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(user_prompt)
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"⚠️ Error: {e}"

    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.session_state.chat_history.append(("assistant", bot_reply))
