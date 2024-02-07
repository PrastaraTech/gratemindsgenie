import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import os
from streamlit_chat import message

import re
import requests

load_dotenv()  # loading all the environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# genai.configure(api_key='AIzaSyBFRJ3Q40xCCdbBKbOSg1Uy3VB49eS8lZM')
model = genai.GenerativeModel(model_name="gemini-pro")
chat = model.start_chat(history=[])

subject_options = {
    "1": ["All", "English", "Mathematics", "EVS", "Hindi", "Art Education", "Computer Education - IT"],
    "2": ["All", "English", "Mathematics", "EVS", "Hindi", "Art Education", "Computer Education - IT"],
    "3": ["All", "English", "Mathematics", "EVS", "Hindi", "Art Education", "Computer Education - IT"],
    "4": ["All", "English", "Mathematics", "EVS", "Hindi", "Art Education", "Computer Education - IT"],
    "5": ["All", "English", "Mathematics", "EVS", "Hindi", "Art Education", "Computer Education - IT"],
    "6": ["All", "English", "Mathematics", "Science", "Social Science", "Hindi", "Sanskrit", "Art Education", "Computer Science"],
    "7": ["All", "English", "Mathematics", "Science", "Social Science", "Hindi", "Sanskrit", "Art Education", "Computer Science"],
    "8": ["All", "English", "Mathematics", "Science", "Social Science", "Hindi", "Sanskrit", "Art Education", "Computer Science"],
    "9": ["All", "English", "Mathematics", "Science", "Social Science", "Hindi", "Sanskrit", "Art Education", "Computer Science", "Health and Physical Education"],
    "10": ["All", "English", "Mathematics", "Science", "Social Science", "Hindi", "Sanskrit", "Art Education", "Computer Science", "Health and Physical Education"],
    "11": ['All', 'Sanskrit', 'Accountancy', 'Chemistry', 'Mathematics', 'Biology', 'Psychology', 'Geography', 'Physics', 'Hindi', 'Sociology', 'English', 'Political Science', 'History', 'Economics', 'Business Studies', 'Home Science', 'Creative Writing and Translation', 'Fine Art', 'Informatics Practices', 'Computer Science', 'Health and Physical Education', 'Biotechnology', 'Sangeet', 'Knowledge Traditions Practices of India'],
    "12": ['All', 'Mathematics', 'Physics', 'Accountancy', 'Sanskrit', 'Hindi', 'English', 'Biology', 'History', 'Geography', 'Psychology', 'Sociology', 'Chemistry', 'Political Science', 'Economics', 'Business Studies', 'Home Science', 'Urdu', 'Creative Writing & Translation', 'Fine Art', 'Computer Science', 'Informatics Practices', 'Biotechnology']
}

sensitive_content_regex = re.compile(
    r"[\(\[](sex|porn|nude|naked|violence|drugs|alcohol)[\)\]]")

# api_key = st.secrets["my_api_key"]


# bard = Bard(token='eAg9X33i8UNIZ-49BT6ibpWS6LTMlashugoRYOdOB8XTStsJBfWGdnVsClWiM8N7c2mA9w.',
#             timeout=30)


st.set_page_config(
    page_title="GrateMinds - Genie",
    page_icon="👋",
    menu_items={
        'Get Help': 'https://prastaratech.com',
        'Report a bug': 'mailto:support@prastaratech.com',
        'About': "# Genie. This is an *extremely* cool app!"
    }
)
st.title("GreatMinds Genie by Prastara")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


@st.cache_data
def response_api(prompt):
    message = ""  # Bard().get_answer(prompt)['content']
    # Filter out sensitive content
    message = sensitive_content_regex.sub('', message)
    return message


user_grade = st.selectbox("Select your grade:",
                          subject_options.keys(), index=None)

if user_grade:
    subject_options_for_grade = subject_options[user_grade]

    user_subject = st.selectbox("Choose your subject",
                                subject_options_for_grade, index=None)

    input = st.text_input("Input: ", key="input")
    submit = st.button("Ask the question")

    prompt = f"Restrict responses only to NCERT textbooks and materials. Refer Class {
        user_grade} subject {user_subject} and give answer to {input}"

    if submit and input:
        response = chat.send_message(prompt, stream=True)
        st.session_state['chat_history'].append(("You", input))
        st.subheader("The Response is")
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot", chunk.text))

    st.subheader("The Chat History is")
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")
