import streamlit as st
import os
import google.generativeai as genai

# Initialize Gemini-Pro
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')


def clear_chat_history():
    st.session_state.chat = model.start_chat(history=[])


def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role


# Add a Gemini Chat history object to Streamlit session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.set_page_config(
    page_title="GrateMinds - Genie",
    page_icon="👋",
    menu_items={
        'Get Help': 'https://prastaratech.com',
        'Report a bug': 'mailto:support@prastaratech.com',
        'About': "# Genie. This is an *extremely* cool app!"
    }
)
# Display Form Title
st.page_link("Hello.py", label="Home", icon="🏠")
st.title(":infinity: Chat with GreatMinds Genie!")
# Display chat messages from history above current input box
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Accept user's next message, add to context, resubmit context to Gemini
if prompt := st.chat_input("What would you like to know?"):
    # Display user's last message
    st.chat_message("user").markdown(prompt)

    # Send user entry to Gemini and read the response
    with st.spinner('Wait...'):
        response = st.session_state.chat.send_message(prompt)

    # Display last
    with st.chat_message("assistant"):
        st.markdown(response.text)
        st.button(':rainbow[Clear History]', on_click=clear_chat_history)
