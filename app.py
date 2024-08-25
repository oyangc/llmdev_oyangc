import streamlit as st

container = st.container()
if "messages" not in st.session_state:
    st.session_state.messages = []
messages = []

prompt = st.chat_input("请输入你要问的问题")
if prompt:
    st.session_state.messages.append(prompt)

with container:
    with st.chat_message("user"):
        for message in st.session_state.messages:
            st.write(message)
