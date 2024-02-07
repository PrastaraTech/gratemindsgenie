import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import os
from streamlit_chat import message

import re
import requests

load_dotenv()  # loading all the environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
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
# st.title("Academics")
st.markdown("# General")
# st.sidebar.title("Academics")


@st.cache_data
def response_api(prompt):
    message = ""  # Bard().get_answer(prompt)['content']
    # Filter out sensitive content
    message = sensitive_content_regex.sub('', message)
    return message


user_text = st.text_area(
    "What are looking for now?")
if user_text:
    if st.button("Ask Genie..."):
        st.toggle("Start fresh?")
        if 'generate' not in st.session_state:
            st.session_state['generate'] = []
        if 'past' not in st.session_state:
            st.session_state['past'] = []

        # output = response_api(f"Restrict responses only to NCERT textbooks and materials. Refer Grade {user_grade} subject {user_subject} and give answer to {user_text}")

        prompt = user_text
        chat.history.append(prompt)
        response = model.generate_content(prompt)
        output = response.text
        chat.history.append(output)
        st.session_state.generate.append(output)
        st.session_state.past.append(str(user_text))

        if st.session_state['generate']:
            for i in range(len(st.session_state['generate']) - 1, -1, -1):
                message(st.session_state['past'][i],
                        is_user=True, key=str(i) + '_user')
                message(st.session_state['generate'][i], key=str(i))
