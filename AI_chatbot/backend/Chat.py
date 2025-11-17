import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

class ChatPage:
    @staticmethod
    def render():
        # Define the CSS to centered and font change the title
        st.markdown(
            """
            <h1 style="font-family: 'Brush Script MT', cursive; text-align: center; color: pink;">
                SUPPORTBOT! 🤖
            </h1>
            """,
            unsafe_allow_html=True # allowed for static such as a title, otherwise don't add
        )

        if 'messages' not in st.session_state:
            st.session_state.messages = []
            st.session_state.messages.append(SystemMessage(""" you are emphatatic stranger, 
            dealing with people who struggle with mental health issues, do not diagnos but give advice 
            and provide basic resource(not referrals but resources). don't write weird roleplaying stuff just be direct, kind, professional, and short answers."""))


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
            model='llama3.2:1b',
            temperature=1

        )
        invoke = LLM.invoke(st.session_state.messages).content

        with st.chat_message("AI"):
            st.markdown(invoke)
            st.session_state.messages.append(AIMessage(invoke))



if __name__ == "__main__":
    ChatPage.render()
