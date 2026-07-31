import streamlit as st
from utils.gemini import health_chat

st.set_page_config(
    page_title="AI Health Chat",
    page_icon="💬",
    layout="wide"
)

st.title("💬 AI Health Chat")

st.write("""
Ask healthcare or medicine-related questions.

Examples:

• Can I take Dolo 650 after food?

• Is Paracetamol safe during pregnancy?

• Can I take Ibuprofen with alcohol?

• Which medicine is used for fever?
""")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
question = st.chat_input("Ask your health question...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
from utils.history import add_history
              answer = health_chat(question)

add_history(
    "AI Chat",
    question,
    answer
)

st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as e:

                st.error("Unable to get response.")

                st.exception(e)

st.markdown("---")

st.warning("""
⚠️ PillVision AI is an educational assistant.

Do not use it for emergencies or as a substitute for professional medical advice.
""")
