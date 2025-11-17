import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


class ChatPage:
    """
    Renders the chat page UI and handles chat message flow.
    Displays a styled title, manages user and AI messages, and calls the LLM for responses.
    """

    @staticmethod
    def render():
        """
        Builds the chat interface, loads past messages, sends new user prompts
        to the LLM, and displays AI responses.
        """

        st.markdown(
            """
            <h1 style="font-family: 'Brush Script MT', cursive; text-align: center; color: pink;">
                SUPPORTBOT! 🤖
            </h1>
            """,
            unsafe_allow_html=True
        )

        if "messages" not in st.session_state:
            st.session_state.messages = []
            st.session_state.messages.append(
                SystemMessage(
                    """
                    write how you would like AI to be
                    """
                )
            )

        for message in st.session_state.messages:
            if isinstance(message, HumanMessage):
                with st.chat_message("User"):
                    st.markdown(message.content)
            elif isinstance(message, AIMessage):
                with st.chat_message("AI"):
                    st.markdown(message.content)

        prompt = st.chat_input("Tell me what is wrong?")

        if prompt:
            with st.chat_message("User"):
                st.markdown(prompt)
            st.session_state.messages.append(HumanMessage(prompt))

        LLM = ChatOllama(
            model="model of ollama used",
            temperature=1
        )

        invoke = LLM.invoke(st.session_state.messages).content

        with st.chat_message("AI"):
            st.markdown(invoke)
        st.session_state.messages.append(AIMessage(invoke))


if __name__ == "__main__":
    ChatPage.render()
