import streamlit as st

from utils.gemini import health_chat
from utils.history import add_history
from utils.pdf import create_pdf

st.set_page_config(
    page_title="AI Health Chat",
    page_icon="💬",
    layout="wide"
)

st.title("💬 AI Health Chat")

st.write("""
Ask medicine and healthcare related questions.

Examples:

• Can I take Dolo 650 after food?

• Is Paracetamol safe during pregnancy?

• Can I take Ibuprofen with alcohol?

• What medicine is used for fever?
""")

# -----------------------------
# Initialize Chat
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Chat
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------

question = st.chat_input("Ask your health question...")

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                answer = health_chat(question)

                st.markdown(answer)

                add_history(
                    "AI Chat",
                    question,
                    answer
                )

                st.session_state.messages.append(
                    {
                        "role":"assistant",
                        "content":answer
                    }
                )

            except Exception as e:

                st.error("Unable to get AI response.")

                st.exception(e)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.header("Chat Options")

if st.sidebar.button("🗑 Clear Chat"):

    st.session_state.messages = []

    st.rerun()

# -----------------------------
# Download Conversation
# -----------------------------

if len(st.session_state.messages) > 0:

    conversation = ""

    for msg in st.session_state.messages:

        conversation += (
            f"{msg['role'].upper()}\n"
            f"{msg['content']}\n\n"
        )

    pdf = create_pdf(conversation)

    with open(pdf, "rb") as file:

        st.sidebar.download_button(
            "📄 Download Chat",
            data=file,
            file_name="AI_Health_Chat.pdf",
            mime="application/pdf"
        )

# -----------------------------
# Examples
# -----------------------------

st.markdown("---")

st.subheader("💡 Suggested Questions")

st.info("""
💊 Can I take Dolo 650 after food?

🤰 Is Crocin safe during pregnancy?

🍺 Can I drink alcohol after taking antibiotics?

🤒 Which medicine is used for fever?

👶 Can children take Paracetamol?
""")

st.markdown("---")

st.warning("""
⚠️ PillVision AI provides educational information only.

Do not use this assistant for emergencies or self-diagnosis.

Always consult a qualified healthcare professional.
""")
