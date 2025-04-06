import streamlit as st
from main import handle_user_input

st.set_page_config(layout="wide", page_title="AI Voice Assistant", page_icon="🎙️")
st.title("🎙️ AI Voice Assistant")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.markdown("**Click the button to speak or type below:**")
col1, col2 = st.columns([1, 5])

with col1:
    if st.button("🎤 Speak"):
        response = handle_user_input(mode="voice")
        if response:
            st.session_state.chat_history.append(("user", response['user']))
            st.session_state.chat_history.append(("assistant", response['assistant']))

with col2:
    user_input = st.text_input("Or type here:", key="text_input")
    if st.button("💬 Submit") and user_input:
        response = handle_user_input(mode="text", user_text=user_input)
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("assistant", response['assistant']))

# Display chat history
for role, msg in st.session_state.chat_history:
    st.markdown(f"**{role.title()}:** {msg}")
