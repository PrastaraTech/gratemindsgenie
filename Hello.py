# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from bardapi import Bard
import os
import extra_streamlit_components as stx
import requests
import streamlit as st
from streamlit_chat import message
import re

# os.environ['_BARD_API_KEY'] = 'bwg9X4yXD1vxejZw4ckJf8HRlRHhiZ3XDmPjJ4u_iQKigoEAl7Gc-uyjZqFQZ2gy0x_AEQ.'
token='bwg9X4yXD1vxejZw4ckJf8HRlRHhiZ3XDmPjJ4u_iQKigoEAl7Gc-uyjZqFQZ2gy0x_AEQ.'

session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
# session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY")) 
session.cookies.set("__Secure-1PSID", token) 
# session.cookies.set_cookie("__Secure-1PSID", token)
session.cookies.get("__Secure-1PSID")
bard = Bard(token=token, session=session, timeout=30)



st.set_page_config(
        page_title="GrateMinds - Genie",
        page_icon="👋",
        menu_items={
                'Get Help': 'https://prastaratech.com',
                'Report a bug': 'mailto:support@prastaratech.com',
                'About': "# Genie. This is an *extremely* cool app!"
                    }
)


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

sensitive_content_regex = re.compile(r"[\(\[](sex|porn|nude|naked|violence|drugs|alcohol)[\)\]]")


@st.cache_resource(experimental_allow_widgets=True)
def get_manager():
    return stx.CookieManager()

cookie_manager = get_manager()

# st.subheader("All Cookies:")
# cookies = cookie_manager.get_all()
# st.write(cookies)
cookie_manager.set("__Secure-1PSID", token)
# st.write("__________________#####################_________________")
# st.write(cookies)

def response_api(prompt):
    message = "" #Bard().get_answer(prompt)['content']
    # Filter out sensitive content
    message = sensitive_content_regex.sub('', message)
    return message

st.title("GreatMinds Genie by Prastara")

user_grade = st.selectbox("Select your grade:",
                           subject_options.keys(), index=None)

if user_grade:
    subject_options_for_grade = subject_options[user_grade]

    user_subject = st.selectbox("Choose your subject",
                                subject_options_for_grade, index=None)

    if user_subject:
        user_text = st.text_input("What are looking for now: ")
        if st.button("Ask Genie..."):
            if 'generate' not in st.session_state:
                st.session_state['generate'] = []
            if 'past' not in st.session_state:
                st.session_state['past'] = []
            
            # output = response_api(f"Restrict responses only to NCERT textbooks and materials. Refer Grade {user_grade} subject {user_subject} and give answer to {user_text}")
           
            prompt = f"Restrict responses only to NCERT textbooks and materials. Refer Grade {user_grade} subject {user_subject} and give answer to {user_text}"
          
            with st.spinner('Wait for it...'):
                # completion = bard.get_answer("Restrict responses only to NCERT textbooks and materials. Refer Grade 4 subject English and get List chapters")['content']
                completion = bard.get_answer(str(prompt))['content']
                
                
                st.session_state.generate.append(completion)
                st.session_state.past.append(str(user_text))

                if st.session_state['generate']:
                    for i in range(len(st.session_state['generate']) - 1, -1, -1):
                        message(st.session_state['past'][i],
                                is_user=True, key=str(i) + '_user')
                        message(st.session_state['generate'][i], key=str(i))




