from dotenv import load_dotenv
import streamlit as st
import os
import textwrap
import google.generativeai as genai

load_dotenv()  # Load environment variables from .env file

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate responses from Gemini
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

# Initialize the Streamlit app
st.set_page_config(page_title="Gemini AI Chatbot", page_icon=":robot_face:")
st.title("🌟 Gemini-Enhanced AI for Mental Health & Emotional Support 🌟")
st.write("Feel free to ask anything. Your mental health matters!")

# User input section
input_text = st.text_area("Your Question:", height=100, placeholder="Type your question here...")

# Button to submit the question
submit_button = st.button("Ask the Question")

# Display response if the button is clicked
if submit_button:
    if input_text.strip():  # Check if the input is not empty
        with st.spinner("Thinking..."):  # Loading spinner
            response = get_gemini_response(input_text)
        st.subheader("🤖 AI Response:")
        st.write(response)
    else:
        st.warning("Please enter a question before submitting.")

# Footer
st.markdown("---")
st.write("Made with ❤️ for your mental health support.")
st.write("**Disclaimer:** This AI is not a substitute for professional mental health advice.")
