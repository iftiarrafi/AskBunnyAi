import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
load_dotenv()

from langchain_groq import ChatGroq

model = ChatGroq(model_name=os.getenv("MODEL_NAME"), groq_api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(
    page_title="QnA Bot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("🐹 AskBunny- Ai QnA Bot")
st.markdown("Your QnA Bot works with LangChain and Groq Model")

if "messages" not in st.session_state:
    st.session_state.messages = []
    

for message in st.session_state.messages:
    role = "user" if isinstance(message,HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(message['content'])


query = st.chat_input("Ask anything...")

if query:
    st.session_state.messages.append(HumanMessage(content=query))
    with st.chat_message("user"):
        st.markdown(query)

    res = model.invoke( st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=res.content))

    with st.chat_message("assistant"):
        st.markdown(res.content)
    