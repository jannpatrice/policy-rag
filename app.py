import streamlit as st

from src.retrieval.rag_service import ask_question

st.set_page_config(
    page_title="Policy Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Policy Assistant")

st.write(
    "Ask questions about company policies."
)

question = st.text_input(
    "Ask a policy question"
)

if st.button("Ask"):

    if question:

        with st.spinner("Searching policies..."):

            answer, docs = ask_question(question)

        # =========================
        # Answer
        # =========================

        st.subheader("Answer")

        st.write(answer)

        # =========================
        # Citations
        # =========================

        st.subheader("Sources")

        for doc in docs:

            with st.expander(doc.metadata["source"]):

                st.write(doc.page_content)