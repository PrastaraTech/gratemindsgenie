import google.generativeai as palm
import streamlit as st
from streamlit_chat import message

import re


st.set_page_config(
    page_title="GrateMinds - Genie",
    page_icon=":sparkles:",
    layout="centered",
    menu_items={
        'Get Help': 'https://prastaratech.com',
        'Report a bug': 'mailto:help@prastaratech.com',
        'About': "# Genie. This is an *extremely* cool app!"
    }
)
st.title("GreatMinds Genie by Prastara")

tab1, tab2, tab3, tab4 = st.columns(4)
with tab1:
    st.page_link("pages/1_Academics.py", icon="💯")
    st.write("""Click :point_up: to get information related to any book or topic in NCERT academic textbooks.""")

with tab2:
    st.page_link("pages/2_QnA-Generator.py", icon="❓")
    st.write(" Click :point_up: to generated question and answers related to any book or topic in NCERT academic textbooks.""")
with tab3:
    st.page_link("pages/3_Chat.py", icon="♾️")
    st.write(
        """ Click :point_up: to start a chat with Ginie on any topic you are interested.""")
with tab4:
    st.page_link("pages/4_Pre-School.py", icon="🌈")
    st.write(
        """ Click :point_up: to start a chat with Ginie on topics related to pre-school education.""")
