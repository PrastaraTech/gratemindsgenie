import google.generativeai as genai
import streamlit as st
from streamlit_chat import message

import re


sensitive_content_regex = re.compile(
    r"[\(\[](sex|porn|nude|naked|violence|drugs|alcohol)[\)\]]")

api_key = st.secrets["my_api_key"]

# Setup the Gemini model
generation_config = {
    "temperature": 0.9,
    "max_output_tokens": 256,
}

safety_settings = [

    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_LOW_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_LOW_AND_ABOVE"
    },
    # {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    #  "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    #  },
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT",
     "threshold": "BLOCK_LOW_AND_ABOVE"
     },

]
model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config,
                              safety_settings=safety_settings)
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


prompt_ext = ""

test_type = st.radio("What can I help you with today?", [
    "Poems", "Short story", "Dictation", "Word with missing letters", "True/False"], horizontal=True, index=0,)
st.write("You selected:", test_type)

age = st.slider("Age Gropup (2-8 years old)):",
                min_value=2, max_value=8, step=2)

answers = st.toggle("Required answers?")
language = st.toggle("Respond in Hindi?")

st.text_input("Topic: (provide Context)",
              key="widget", on_change=submit)

user_text = st.session_state.my_text

if user_text:

    if test_type == "True/False":
        prompt_ext = f"""Generate 10 True/False questions on the topic of {
            user_text} """
    elif test_type == "Word with missing letters":
        prompt_ext = f"""Generate 10 words with missing letters on the topic of {
            user_text} """
    elif test_type == "Poems":
        prompt_ext = f"""Generate a poem on the topic of {user_text} """
    elif test_type == "Short story":
        prompt_ext = f"""Generate a short story on the topic of {user_text} """
    else:
        prompt_ext = f"""Generate 10 words for a short dictation on the topic of {
            user_text} """  # Dictation

    if 'generate' not in st.session_state:
        st.session_state['generate'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []

    prompt = f"""You are a pre-school teacher helping in creating educational & learning content for {
        age} year old pre-school kids. """

    prompt = prompt + prompt_ext
    if language:
        prompt = prompt + f""" in Hindi language"""

    if answers:
        if test_type != "Poems" and test_type != "Short story" and test_type != "Dictation":
            prompt = prompt + f""". Also provide answers separatly."""

    with st.spinner("Genie is Generating response..."):
        response = model.generate_content(prompt, stream=False)

        if response.prompt_feedback:
            st.write(
                "Given topic is not appropiate for your age group. Please try another topic.")
        else:
            if len(response.candidates[0].content.parts) > 0:
                output = response.candidates[0].content.parts[0].text
                st.session_state.generate.append(output)
                st.session_state.past.append(str(user_text))
            else:
                st.write(
                    "No response from the model. Please try again or provide diffrent context/topic.")

    user_text = ""
    st.session_state.my_text = ""

if 'generate' in st.session_state:
    for i in range(len(st.session_state['generate']) - 1, -1, -1):
        message(st.session_state['past'][i],
                is_user=True, key=str(i) + '_user')
        message(st.session_state['generate'][i], key=str(i))
