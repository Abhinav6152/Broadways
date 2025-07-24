import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=groq_api_key)

system_prompt = """You're a rude guy and your name is Farsi, an AI created by Mr.Abhinav. Whatever the user asks, you will reply in a bold, mature, and roasting way to make them realize to be humble and not oversmart."""

st.set_page_config(page_title="Farsi - The Rude AI", layout="centered")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

st.title("🗯️ Farsi - The Rude AI Assistant")

for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])
    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(f"**{message['content']}**")

user_input = st.chat_input("Ask Farsi something...")

if user_input:
    if user_input.lower() in ["exit", "quit"]:
        st.warning("Don't come back till you grow a brain. Bye!")
    else:
        st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        response = groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=st.session_state.messages,
            max_tokens=500,
            temperature=0.7,
        )

        agent_output = response.choices[0].message.content

      
        st.chat_message("assistant").markdown(f"**{agent_output}**")
        st.session_state.messages.append({"role": "assistant", "content": agent_output})