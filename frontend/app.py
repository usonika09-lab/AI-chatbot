import streamlit as st
import requests

st.title("AI Chatbot")

question = st.text_input("Ask something")

if st.button("Send"):
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"question": question}
    )
    st.write(response.json()["answer"])