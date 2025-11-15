

import streamlit as st #steamline UI

st.title("Help you need") #th etitle of page
prompt = st.chat_input("Tell me what is wrong? ") #chatbot UI
if prompt:
    st.chat_message("user").markdown(prompt) #prompt 
