import google.generativeai as genai
import streamlit as st
from streamlit_chat import message

import re


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

api_key = st.secrets["my_api_key"]

model = genai.GenerativeModel(model_name="gemini-pro")
chat = model.start_chat(history=[])

st.set_page_config(
    page_title="GrateMinds - Genie",
    page_icon="👋",
    menu_items={
        'Get Help': 'https://prastaratech.com',
        'Report a bug': 'mailto:support@prastaratech.com',
        'About': "# Genie. This is an *extremely* cool app!"
    }
)
st.page_link("Hello.py", label="Home", icon="🏠")
st.markdown("# QnA Generator from Academic Textbooks :question:")


@st.cache_data
def response_api(prompt):
    message = ""  # Bard().get_answer(prompt)['content']
    # Filter out sensitive content
    message = sensitive_content_regex.sub('', message)
    return message


if "my_text" not in st.session_state:
    st.session_state.my_text = ""


def submit():
    st.session_state.my_text = st.session_state.widget
    st.session_state.widget = ""


user_grade = st.selectbox("Select your grade:",
                          subject_options.keys(), index=None)

if user_grade:
    subject_options_for_grade = subject_options[user_grade]

    user_subject = st.selectbox("Choose your subject",
                                subject_options_for_grade, index=0)

    if user_subject:
        test_type = st.radio("What type of test?", [
                             "Questions", "MCQ", "Fill in the blanks"], horizontal=True, index=0,)
        st.write("You selected:", test_type)

        questions = st.slider("Number of questions:",
                              min_value=2, max_value=10, step=2)

        answers = st.toggle("Required answers?")

        st.text_input("Topic: (provide unit/chapter/lession name)",
                      key="widget", on_change=submit)

        user_text = st.session_state.my_text
        if user_text:
            if 'generate' not in st.session_state:
                st.session_state['generate'] = []
            if 'past' not in st.session_state:
                st.session_state['past'] = []

            prompt = f"""Restrict responses only to NCERT textbooks and materials. Refer '{user_subject}' textbook of Grade {
                user_grade} and generate {questions} {test_type} type questions related to '{user_text}'"""

            if answers:
                prompt = prompt + " also provide answers separatly."

            with st.spinner():
                response = model.generate_content(prompt)
                output = response.text

            st.session_state.generate.append(output)
            st.session_state.past.append(str(user_text))
            user_text = ""
            st.session_state.my_text = ""

if 'generate' in st.session_state:
    for i in range(len(st.session_state['generate']) - 1, -1, -1):
        message(st.session_state['past'][i],
                is_user=True, key=str(i) + '_user')
        message(st.session_state['generate'][i], key=str(i))
