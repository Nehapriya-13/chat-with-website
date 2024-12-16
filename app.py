import os

# Set USER_AGENT environment variable
os.environ['USER_AGENT'] = 'MyCustomUserAgent/1.0'


import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage 
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from utils import get_vectorstore_from_url, get_context_retriever_chain, get_conversational_rag_chain, get_response

st.set_page_config(page_title='Chat with website', page_icon='🧠')
st.title('Chat with website')
website_url = st.text_input("https://c:/Users/nehap/Downloads/website/app.py.com")

if website_url is None or website_url == "https://c:/Users/nehap/Downloads/website/app.py.com":
    st.info("https://c:/Users/nehap/Downloads/website/app.py.com")

else:

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hello, I'm a bot. How can I help you today?"),
        ]

    if "vector_store" not in st.session_state:
        st.session_state.vector_store = get_vectorstore_from_url("https://c:/Users/nehap/Downloads/website/app.py.com")  



    user_query = st.chat_input("Type your mesage here ...")

    if user_query is not None and user_query != "":w
    response = get_response(user_query)
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    st.session_state.chat_history.append(AIMessage(content=response))

    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message,  HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)