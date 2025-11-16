import streamlit as st

class StateManager:
    @staticmethod
    def initialize():
        if "page" not in st.session_state:
            st.session_state.page = "chat"
        if "mood_data" not in st.session_state:
            st.session_state.mood_data = []

    @staticmethod
    def set_page(page_name: str):
        st.session_state.page = page_name

    @staticmethod
    def add_mood_entry(entry: dict):
        st.session_state.mood_data.append(entry)

    @staticmethod
    def get_mood_data():
        return st.session_state.mood_data
