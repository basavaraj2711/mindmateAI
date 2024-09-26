import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from pathlib import Path

# Set the page configuration
st.set_page_config(page_title="Gemini-Enhanced AI for Mental Health & Emotional Support", page_icon=":robot_face:")

# Load environment variables
load_dotenv()

# Configure the Gemini/PaLM API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to start a chat and get responses
def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat(history=[])

    # Send the user's message and get the response
    response = chat.send_message(question, stream=True)

    # Create a complete response by joining the chunks
    return "".join(chunk.text for chunk in response)  # Combine all response chunks

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .title-style {
        font-family: 'Verdana';
        color: #4b72ff;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 20px;
    }
    .logo-style {
        display: block;
        margin: 0 auto;
    }
    .chat-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    .user-message {
        font-weight: bold;
        color: #2196f3;
        margin-top: 10px;
    }
    .bot-message {
        color: #4CAF50;
        margin-top: 10px;
    }
    .stTextArea {
        border-radius: 8px;
        border: 2px solid #4b72ff;
    }
    </style>
""", unsafe_allow_html=True)

# Navbar for different functionalities
st.sidebar.title("Solutions Which Can Help you")
page = st.sidebar.selectbox("Choose how we can help you:", ["Chatbot", "Mindfulness & Meditation", "Anonymous Help Requests", "Success Stories", "Feelings Questionnaire", "Healthcare Resources"])

# Center the logo using Streamlit columns
logo_path = Path(r"C:/Users/Hp/OneDrive/Desktop/End-To-End-Gemini-Project/Screenshot 2024-09-24 141917.png")


# Display the title and logo
st.markdown('<div class="title-style">🌟 You deserve to be happy. 🌟</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

# Place the logo in the middle column
with col2:
    st.image(str(logo_path), width=50, caption="MindMate AI AI", output_format="PNG", use_column_width=True)

# Functionality for Chatbot Page
if page == "Chatbot":
    st.markdown("#### 🤖 Let me help you, tell me how you are feeling:")

    example_questions = [
        "I'm feeling down, how can I lift my mood?",
        "How do I manage anxiety in difficult situations?",
        "What are some ways to feel more positive?",
        "I feel overwhelmed by stress. Can you help?",
        "How can I calm my anxiety attacks?",
        "What are techniques for self-care?",
        "I feel lonely. What can I do?"
    ]

    selected_question = st.selectbox("Or choose a question to ask:", [""] + example_questions)
    input_text = st.text_area("Your Question:", value=selected_question, height=100, placeholder="💬 Type your question here...")
    submit_button = st.button("🚀 Ask the Question to MindMate AI")
    clear_button = st.button("🗑️ Clear Chat History")

    # Initialize session state for chat history and previous responses if they don't exist (for chatbot)
    if 'chatbot_history' not in st.session_state:
        st.session_state['chatbot_history'] = []
    if 'chatbot_responses' not in st.session_state:
        st.session_state['chatbot_responses'] = set()

    # Clear chat history if button is pressed
    if clear_button:
        st.session_state['chatbot_history'] = []
        st.session_state['chatbot_responses'] = set()
        st.success("Chatbot history cleared!")

    # Chat area styling with user and bot messages
    if submit_button:
        if input_text.strip():  # Check if input is not empty
            with st.spinner("MindMateAI Thinking... 🤖"):
                response = get_gemini_response(input_text)

                # Ensure the response is unique
                if response not in st.session_state['chatbot_responses']:
                    st.session_state['chatbot_responses'].add(response)
                    st.session_state['chatbot_history'].insert(0, ("You", input_text))  # Add to the front for latest first
                    st.session_state['chatbot_history'].insert(0, ("Bot", response))

    # Display chat history for chatbot
    if st.session_state['chatbot_history']:
        st.markdown("---")
        st.markdown('<h4 style="text-align:center;">📝 Chatbot History:</h4>', unsafe_allow_html=True)
        for role, text in st.session_state['chatbot_history']:
            if role == "You":
                st.markdown(f'<div class="chat-box user-message">👤 **{role}:** {text}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-box bot-message">🤖 **{role}:** {text}</div>', unsafe_allow_html=True)

# ------------------------------ #
# 1. Mindfulness & Meditation Page #
# ------------------------------ #
elif page == "Mindfulness & Meditation":
    st.markdown("### 🧘‍♂️ Mindfulness & Meditation")
    st.markdown("""
        Explore mindfulness and meditation resources designed to help you relax and manage stress.
        
        #### Popular Guided Meditations:
        - **10-Minute Mindfulness Meditation**  
          [Watch on YouTube](https://www.youtube.com/watch?v=inpok4MKVLM)
        
        - **Breathing Exercises for Stress Relief**  
          [Watch on YouTube](https://www.youtube.com/watch?v=sJ04nsiz_Mc)
        
        #### Audio Relaxation:
        - [Soothing Rain Sounds](https://example.com/rain.mp3)
        - [Calming Nature Sounds](https://example.com/nature.mp3)
    """)
    
    st.video("https://www.youtube.com/watch?v=inpok4MKVLM")
    st.video("https://www.youtube.com/watch?v=d96akWDnx0w&ab_channel=Motiversity") 
    st.video("https://www.youtube.com/watch?v=ec63EDhTvN4&ab_channel=BenLionelScott")  # Example embedded video
  

# ---------------------------- #
# 2. Anonymous Help Requests Page #
# ---------------------------- #
elif page == "Anonymous Help Requests":
    st.markdown("### 📝 Anonymous Help Requests")
    
    st.markdown("Feel free to share your questions or concerns anonymously. Our team will respond in blog format or video responses.")
    
    # Input form for anonymous help request
    anonymous_question = st.text_area("Your Anonymous Question or Concern", height=150, placeholder="Type your question here...")
    submit_help_request = st.button("Submit Anonymously")
    
    if submit_help_request and anonymous_question.strip():
        if 'anonymous_requests' not in st.session_state:
            st.session_state['anonymous_requests'] = []
        
        st.session_state['anonymous_requests'].append(anonymous_question)
        st.success("Your anonymous request has been submitted!")
    
    # Displaying previously submitted anonymous requests
    if 'anonymous_requests' in st.session_state:
        st.markdown("### 📝 Submitted Requests:")
        for idx, request in enumerate(st.session_state['anonymous_requests'], 1):
            st.markdown(f"**Request {idx}:** {request}")

# ------------------------- #
# 3. Success Stories Page #
# ------------------------- #
elif page == "Success Stories":
    st.markdown("### 💪 Success Stories")
    st.markdown("Read inspiring stories from individuals who have overcome emotional challenges.")
    
    # Pre-defined success stories
    success_stories = [
    {
        "name": "Tara",
        "story": (
            "I was in a deep hole. Over a period of about two months, I fell into a deep hole of "
            "depression when several issues came to a head in my life. It all began when schoolwork "
            "started to get difficult. After years of easy grades, I suddenly had to work hard for them, "
            "and the requirements became more complex and intense. After a while, I gave up trying, as "
            "I convinced myself that I just couldn't do it. I felt lost and confused, with no idea of "
            "what I wanted for the future. I lost all motivation. I thought that by giving up and "
            "ignoring the difficult things, life would get easier.\n\n"
            "Gradually, I became increasingly unhappy with myself, affecting my relationships with family "
            "and close friends. I became very removed and distant. My emotions became more intense, and I "
            "fell deeper into a black hole of depression. Although I maintained a smile, I was screaming "
            "inside for someone to notice my unhappiness.\n\n"
            "My sadness turned to anger, and I became angry at the world, at myself, and at everyone else. "
            "I took my anger out on my family, constantly fighting with my Mum. I spent a lot of time alone "
            "in my room, listening to music and crying, trying to escape from the world.\n\n"
            "I found an outlet for my emotions in writing and drawing. By spilling it all out on paper, I "
            "could think more clearly and make sense of how I felt.\n\n"
            "The situation started to get better when I finally began to talk about it. Suddenly, it didn’t "
            "seem so bad after all. I opened up to a friend, and after all the tears and emotion, I realized "
            "that people cared about me. It was like a huge weight had been lifted from my shoulders.\n\n"
            "I learned a lot about life as I gradually overcame my depression. It’s not easy, but it's not "
            "meant to be easy. It's the challenging times and experiences that make us better and stronger people.\n\n"
            "Although I still don't know exactly what I want to do in life, I’ve realized that if you do "
            "things that make you happy, you’ll get somewhere you want to be and find happiness along the way."
        )
    },
    # Add other success stories here
    {
         "name": "James",
            "story": (
                "After losing my job unexpectedly, I went through a phase of intense anxiety and fear. I didn’t "
                "know how I would pay my bills or support my family. The weight of uncertainty felt like it was "
                "crushing me. I was terrified to even leave my house.\n\n"
                "I decided to seek support from my friends and family. They listened to my concerns and helped me "
                "develop a plan to look for new opportunities. With their encouragement, I started practicing "
                "mindfulness and meditation to manage my anxiety. It took time, but gradually I regained my "
                "confidence.\n\n"
                "Now, I have a new job that I love, and I feel more resilient than ever. I learned that asking for "
                "help is a strength, not a weakness."
            )
    }
]

    
    for story in success_stories:
       with st.container():
        # Highlight the name
        st.markdown(f"### **{story['name']}**")
        
        # Add a box around the story
        st.markdown(
            f"<div style='border: 1px solid #d9d9d9; border-radius: 5px; padding: 15px; background-color: #000000;'>"
            f"{story['story']}</div>",
            unsafe_allow_html=True
        )
        
        # Add space between stories
        st.markdown("<br>", unsafe_allow_html=True)

# Functionality for Feelings Questionnaire Page
elif page == "Feelings Questionnaire":
    st.markdown("#### 🤔 You can click on the following options and I will try to help you in all possible ways")

    feelings = [
        "I feel anxious or worried.",
        "I feel sad or depressed.",
        "I feel overwhelmed with stress.",
        "I feel lonely or isolated.",
        "I feel angry or frustrated."
    ]

    responses = {feeling: st.checkbox(feeling) for feeling in feelings}
    submit_responses_button = st.button("📝 Submit My Feelings")
    clear_feelings_button = st.button("🧹 Clear Responses")

    if submit_responses_button:
        st.success("Your responses have been submitted!")

    if clear_feelings_button:
        st.session_state['feelings_responses'] = {}
        st.success("Your responses have been cleared!")

# -------------------------- #
# 4. Healthcare Resources Page #
# -------------------------- #
elif page == "Healthcare Resources":
    st.markdown("### 📞 Healthcare Contacts & Resources")
    st.markdown("""
    Here are some important contacts and resources that you can reach out to:

    #### Important Contacts:
    - **National Suicide Prevention Lifeline**: 1-800-273-TALK (1-800-273-8255)
    - **Crisis Text Line**: Text "HELLO" to 741741
    - **Substance Abuse and Mental Health Services Administration (SAMHSA)**: 1-800-662-HELP (1-800-662-4357)
    - **National Alliance on Mental Illness (NAMI)**: 1-800-950-NAMI (6264)
    - **Mental Health America**: 1-800-969-6642

    #### Recommended Therapists & Resources:
    - **[Psychology Today Therapist Directory](https://www.psychologytoday.com/us/therapists)**: Find licensed therapists, psychologists, and counselors in your area.
    - **[BetterHelp](https://www.betterhelp.com)**: Access online therapy sessions with licensed professionals tailored to individual needs.
    - **[Talkspace](https://www.talkspace.com)**: Provides online therapy and counseling.
    - **[GoodTherapy](https://www.goodtherapy.org/)**: Search for therapists, counselors, and mental health professionals based on your specific needs.
    - **[Open Path Psychotherapy Collective](https://openpathcollective.org/)**: Affordable in-person and online therapy sessions with licensed mental health professionals.
    - **[TherapyRoute.com](https://www.therapyroute.com/)**: Connect with therapists, psychologists, and psychiatrists worldwide.

    #### Apps for Mental Health:
    - **[Headspace](https://www.headspace.com)**: Meditation and mindfulness exercises for stress and anxiety relief.
    - **[Calm](https://www.calm.com)**: Meditation, relaxation, and sleep improvement app.
    - **[Moodfit](https://www.getmoodfit.com)**: Helps you improve your mood and mental health.
    - **[Calm Harm](https://calmharm.co.uk/)**: An app providing tasks that help users manage the urge to self-harm.

    #### Open Source & Social Media Platforms:
    - **[Mental Health Reddit Communities](https://www.reddit.com/r/mentalhealth/)**: A supportive community discussing mental health topics, personal experiences, and coping strategies.
    - **[Mental Health Twitter](https://twitter.com/search?q=mentalhealth&src=typed_query)**: Follow hashtags like #MentalHealth, #TherapyTwitter, and #MentalHealthMatters to connect with mental health advocates, therapists, and professionals.
    - **Facebook Groups**: Search for "Mental Health Support" on Facebook to find local groups and online communities for mental health support.

    #### Open Source Mental Health Resources:
    - **[Mental Health America Screening Tools](https://screening.mhanational.org/screening-tools)**: Free, confidential mental health screening tools for anxiety, depression, PTSD, and more.
    - **[Mind](https://www.mind.org.uk/)**: Offers information and advice on mental health conditions, treatment options, and self-care tips.
    - **[Open Sourcing Mental Illness (OSMI)](https://osmihelp.org/)**: Resources and support focusing on mental health in the tech and open-source community.
    - **[National Alliance on Mental Illness (NAMI)](https://www.nami.org/Home)**: Offers support groups, educational resources, and connections to local mental health services.

    #### Recommended Websites:
    - **[Smiling Mind](https://www.smilingmind.com.au)**: Free mindfulness app for people of all ages.
    - **[Mental Health Foundation](https://www.mentalhealth.org.uk)**: Provides information and resources for mental health awareness.
    - **[Verywell Mind](https://www.verywellmind.com)**: A comprehensive resource for mental health topics.
    """)


# Add footer if needed
st.markdown("---")
st.markdown("<h5 style='text-align: center;'>© 2024 Emotional Support By Gemini. All Rights Reserved.</h5>", unsafe_allow_html=True)
