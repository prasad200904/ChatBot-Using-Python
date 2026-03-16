import streamlit as st
from main import get_ai_response, SYSTEM_MESSAGE

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

st.title("🤖 AI Chatbot")
st.write("Chat with your AI assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [SYSTEM_MESSAGE]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                reply = get_ai_response(st.session_state.messages)
                st.markdown(reply)

        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )

    except Exception as e:
        st.error(f"Error: {e}")