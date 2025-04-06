import streamlit as st
from assistant.core import generate_response
from utils.speech import record_audio, speak_text
from utils.text_chat import text_chat_interface
from assistant.memory import save_chat_history, load_chat_history

st.set_page_config(page_title="AI Voice Assistant", layout="centered", page_icon="🎙️")
st.title("🎙️ AI Voice & Text Assistant")

# Chat History Setup
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = load_chat_history()

# Display chat history
for user, bot in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(user)
    with st.chat_message("assistant"):
        st.markdown(bot)

# Voice Input Button
if st.button("🎙️ Record Voice"):
    st.info("Recording... Please speak")
    voice_input = record_audio()
    st.chat_message("user").markdown(voice_input)
    bot_response = generate_response(voice_input)
    st.chat_message("assistant").markdown(bot_response)
    speak_text(bot_response)
    st.session_state.chat_history.append((voice_input, bot_response))
    save_chat_history(st.session_state.chat_history)

# Fallback Text Chat
with st.expander("💬 Or use Text Chat"):
    text_chat_interface()
