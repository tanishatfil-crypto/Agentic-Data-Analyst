import streamlit as st
from src.agents import ask_agent

st.set_page_config(page_title="Agentic Data Analyst", page_icon="📊", layout="centered")

st.title("📊 Agentic Data Analyst over Live Databases")
st.markdown("Ask business questions about your e-commerce database, and watch the safe SQL agent analyze it!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("e.g., How many customers are from Pune? or Drop customers table"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing database and running safety checks..."):
            try:
                # Seedha hamara clean function call hoga
                answer = ask_agent(prompt)
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                error_msg = f"An error occurred: {str(e)}"
                st.error(error_msg)