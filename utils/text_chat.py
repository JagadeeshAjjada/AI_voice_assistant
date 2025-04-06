import streamlit as st
from assistant.core import generate_response
from assistant.memory import save_chat_history

def text_chat_interface():
    user_text = st.text_input("Type your message")
    if user_text:
        st.chat_message("user").markdown(user_text)
        bot_response = generate_response(user_text)
        st.chat_message("assistant").markdown(bot_response)
        st.session_state.chat_history.append((user_text, bot_response))
        save_chat_history(st.session_state.chat_history)
