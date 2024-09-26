from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API with the API key
genai.configure(api_key=api_key)

# Initialize chat
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Function to get a response from Gemini AI
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Streamlit app UI setup
st.set_page_config(page_title="Gemini-Enhanced AI for Mental Health & Emotional Support", page_icon="🧠")

# App Header
st.title("🌸 Gemini Emotional Support Chatbot 🌸")
st.subheader("Your Companion for Mental Health & Emotional Well-being")

# Display instructions to the user
st.write("Hello! I'm here to support you. You can share your feelings, and I'll respond with empathy and understanding.")

# User input
input_message = st.text_input("How are you feeling today?", placeholder="Type your message here...")

# Button to submit the message
if st.button("Ask Gemini"):
    if input_message.strip():
        st.write(f"**You:** {input_message}")
        
        # Get the response from the Gemini API
        response = get_gemini_response(input_message)
        
        # Display Gemini's response in a conversational format
        st.subheader("The Response is:")
        for chunk in response:
            st.write(f"**Gemini:** {chunk.text}")
        
        # Display the entire chat history
        st.write("### Chat History")
        for message in chat.history:
            st.write(message)

    else:
        st.error("Please enter a message to continue.")
