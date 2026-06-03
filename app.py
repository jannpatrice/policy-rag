import streamlit as st

from src.retrieval.rag_service import ask_question

st.set_page_config(
    page_title="Policy Assistant",
    page_icon="📚"
)

st.title("📚 Policy Assistant")

question = st.text_input(
    "Ask a policy question"
)

if st.button("Ask"):

    if question:

        with st.spinner("Searching policies..."):

            answer, sources = ask_question(question)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Sources")

        for source in sources:
            st.write(f"- {source}")