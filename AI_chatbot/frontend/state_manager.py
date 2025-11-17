'''from langchain_community.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama
'''

import streamlit as st


class StateManager:
    """
    A class that manages all Streamlit session state variables.
    Provides static methods so the class doesn't need to be instantiated.
    """

    @staticmethod
    def initialize():
        """
        Initializes required session_state keys.
        Ensures 'page' and 'mood_data' exist to avoid errors.
        """
        if "page" not in st.session_state:
            st.session_state.page = "chat"

        if "mood_data" not in st.session_state:
            st.session_state.mood_data = []

    @staticmethod
    def set_page(page_name: str):
        """
        Sets the current active page in session_state.
        """
        st.session_state.page = page_name

    @staticmethod
    def add_mood_entry(entry: dict):
        """
        Appends a new mood entry (dictionary) to mood_data.
        """
        st.session_state.mood_data.append(entry)

    @staticmethod
    def get_mood_data():
        """
        Returns all stored mood entries.
        """
        return st.session_state.mood_data
