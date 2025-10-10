import os
import streamlit as st
#from dotenv import load_dotenv
from google import genai

# Load environment variables
#load_dotenv()

# Configure Streamlit
st.set_page_config(
    page_title="Chat With Gemini 2.5 Pro",
    page_icon="🤖",
    layout="centered",
)

# Get API key
#GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

if not GOOGLE_API_KEY:
    st.error("⚠️ GOOGLE_API_KEY not found in .env file.")
    st.stop()

# Configure client
genai_client = genai.Client(api_key=GOOGLE_API_KEY)

# Select best model
MODEL_NAME = "models/gemini-2.5-pro"

# Create chat session if not present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("💬 Gemini Pro Chatbot")

# Display previous messages
for role, content in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(content)

# Chat input
user_prompt = st.chat_input("Ask Gemini something...")
if user_prompt:
    # Display user message
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append(("user", user_prompt))

    # Generate response
    try:
        response = genai_client.models.generate_content(
            model=MODEL_NAME,
            contents=user_prompt
        )
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"⚠️ Error: {str(e)}"

    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.session_state.chat_history.append(("assistant", bot_reply))