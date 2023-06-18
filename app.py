import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'
messages = [{"role": "system", "content": "You are an intelligent assistant."}]

st.title("ChatGPT with Streamlit")

# Input field for user message
user_input = st.text_input("User:")

if user_input:
    messages.append({"role": "user", "content": user_input})
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = chat.choices[0].message.content
    st.text(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

