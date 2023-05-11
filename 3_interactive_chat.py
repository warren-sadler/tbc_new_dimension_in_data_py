from dotenv import load_dotenv
import streamlit as st
from streamlit_chat import message as st_message
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage, HumanMessage


@st.cache_resource
def load_model():
    load_dotenv()
    model = OpenAI()
    chat = ConversationChain(llm=model ,memory=ConversationBufferMemory())
    chat.prompt.template = """
    You are a ReactJS expert answer the following questions as tersely as possible.
    {history}
    User: {input}
    AI:
    """
    return chat

st.title("Talk to your ⚛️ Expert")

if "history" not in st.session_state:
    st.session_state.history = []
    
    
def handle_change():
    chat = load_model()
    question = st.session_state.question
    res = chat.run(question)
    st.session_state.history.append({'message': question, 'is_user': True})
    st.session_state.history.append({'message': res, 'is_user': False})
    st.session_state.question = ""
    
st.text_input("What is your question?", key="question", on_change=handle_change)

for i,msg in enumerate(st.session_state.history):
    st_message(**msg, key=str(i))