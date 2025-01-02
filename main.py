import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint

import config

# Initialize HuggingFace endpoint (ensure config.py is set up)
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=128, temperature=0.7, token=config.SECRET_KEY)

st.set_page_config(page_title="ChatGPT Clone with Streamlit", page_icon=":robot:")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get LLM response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = llm.invoke(prompt)
            st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})