import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import os
from streamlit_chat import message

import csv


with open('NCERT.txt', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    data = []
    for row in reader:
        # Access data using column names
        data.append(row)

    # Get distinct values from Grade column
    distinct_grades = set(row["Grade"] for row in data)
    # Convert the set to a list
    grades_list = sorted(list(distinct_grades))
    print(grades_list)

load_dotenv()  # loading all the environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# genai.configure(api_key='AIzaSyBFRJ3Q40xCCdbBKbOSg1Uy3VB49eS8lZM')
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
                          grades_list, index=None)

if user_grade:
    grade_rows = []
    for row in data:
        if row["Grade"] == user_grade:
            grade_rows.append(row)

    # Get distinct values from Grade column
    distinct_subjects = set(row["Subject"] for row in grade_rows)
    # Convert the set to a list
    subjects_list = sorted(list(distinct_subjects))

    user_subject = st.selectbox("Choose your subject",
                                subjects_list, index=None)

    if user_subject:
        textbook_rows = []
        for row in grade_rows:
            if row["Grade"] == user_grade and row["Subject"] == user_subject:
                textbook_rows.append(row)

        # Get distinct values from Textbook column
        distinct_textbooks = set(row["Textbook"] for row in textbook_rows)
        # Convert the set to a list
        textbook_list = sorted(list(distinct_textbooks))

        user_textbook = st.selectbox("Choose textbook name",
                                     textbook_list, index=None)

        if user_textbook:
            input = st.text_input("Input: ", key="input")
            submit = st.button("Ask the question")

            prompt = f"""
            Don't give any responses which are unsafe for kids below 16 years.
            Try to limit responses to NCERT or byjus.com textbooks and materials.
            Provide: '{input}', by following below criteria
            Class: {user_grade}
            Subject: {user_subject}
            Textbook name: {user_textbook}.
            """

            if submit and input:
                prompt
                response = chat.send_message(prompt, stream=True)
                st.session_state['chat_history'].append(("You", input))
                st.subheader("The Response is")
                for chunk in response:
                    st.write(chunk.text)
                    st.session_state['chat_history'].append(
                        ("Bot", chunk.text))

            st.subheader("The Chat History is")
            for role, text in st.session_state['chat_history']:
                st.write(f"{role}: {text}")
