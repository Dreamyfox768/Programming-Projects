import streamlit as st
from state_manager import StateManager
from chat_page import ChatPage
from mood_page import MoodPage


class app:
    """
    Main application controller.
    Renders the sidebar navigation and switches between the Chat page
    and Mood Tracker page based on user selection.
    """

    st.markdown(
        """
        <h1 style="font-family: 'Brush Script MT', cursive; position: fixed; color: pink; font-size: Large;">
            Options 👆
        </h1>
        """,
        unsafe_allow_html=True
    )

    StateManager.initialize()
    st.sidebar.title("Navigation")

    if st.sidebar.button("AI Chat"):
        StateManager.set_page("chat")

    if st.sidebar.button("Mood Tracker"):
        StateManager.set_page("mood")

    if st.session_state.page == "chat":
        ChatPage.render()

    elif st.session_state.page == "mood":
        MoodPage.render()
