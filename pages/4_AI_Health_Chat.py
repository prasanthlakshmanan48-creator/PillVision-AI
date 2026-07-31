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

st.markdown("""
Ask medicine and healthcare-related questions.

### Example Questions

• Can I take Dolo 650 after food?

• Is Paracetamol safe during pregnancy?

• Can I take Ibuprofen with alcohol?

• Which medicine is used for fever?

• What are the side effects of Azithromycin?
""")

st.markdown("---")

# ==============================
# Chat History
# ==============================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ==============================
# Display Previous Messages
# ==============================

for msg in st.session_state.chat_history:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ==============================
# User Input
# ==============================

question = st.chat_input(
    "Ask your health question..."
)

if question:

    st.session_state.chat_history.append({
        "role":"user",
        "content":question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                answer = health_chat(question)

                st.markdown(answer)

                st.session_state.chat_history.append({
                    "role":"assistant",
                    "content":answer
                })

                add_history(
                    "AI Chat",
                    question,
                    answer
                )

            except Exception as e:

                st.error("Unable to generate response.")

                st.exception(e)

st.markdown("---")

# ==============================
# Sidebar
# ==============================

st.sidebar.header("⚙ Chat Options")

if st.sidebar.button("🗑 Clear Chat"):

    st.session_state.chat_history = []

    st.rerun()

if len(st.session_state.chat_history)>0:

    conversation=""

    for msg in st.session_state.chat_history:

        conversation += (
            f"{msg['role'].upper()}\n"
            f"{msg['content']}\n\n"
        )

    pdf=create_pdf(conversation)

    with open(pdf,"rb") as file:

        st.sidebar.download_button(
            "📄 Download Chat PDF",
            file,
            file_name="AI_Health_Chat.pdf",
            mime="application/pdf"
        )

st.sidebar.markdown("---")

st.sidebar.info("""
Suggested Topics

💊 Medicine Uses

🤰 Pregnancy Safety

🍺 Alcohol Interaction

🥛 Food Interaction

💉 Dosage

⚠ Side Effects
""")

st.markdown("---")

st.subheader("💡 Suggested Questions")

col1,col2=st.columns(2)

with col1:

    st.info("""
💊 Can I take Dolo 650 after food?

🤒 What medicine is used for fever?

🤰 Is Crocin safe during pregnancy?
""")

with col2:

    st.info("""
🍺 Can I drink alcohol after antibiotics?

👶 Can children take Paracetamol?

💊 What are the side effects of Cetirizine?
""")

st.markdown("---")

st.warning("""
⚠ PillVision AI provides educational information only.

Do not use this application for emergency medical situations.

Always consult a qualified healthcare professional.
""")
