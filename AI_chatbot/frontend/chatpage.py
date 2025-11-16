import streamlit as st

class ChatPage:
    @staticmethod
    def render():
        st.markdown(
            """
            <h1 style="font-family: 'Brush Script MT', cursive; text-align: center; color: pink;">
                Help You Need
            </h1>
            """,
            unsafe_allow_html=True
        )

        if 'messages' not in st.session_state:
            st.session_state.messages = []

        prompt = st.chat_input("Tell me what is wrong?")

        if prompt:
            st.session_state.messages.append({'role': "user", 'content': prompt})
            response = "I'm here to help. Let's figure it out together!"  # This should be dynamic in a real scenario
            st.session_state.messages.append({'role': "AI", 'content': response})

        for message in st.session_state.messages:
            st.chat_message(message['role']).markdown(message['content'])

if __name__ == "__main__":
    ChatPage.render()
