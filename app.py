import streamlit as st
import os
import tempfile
from pdf_qa import get_vectorstore, get_deep_summary

st.set_page_config(page_title="SmartDoc Summarizer", layout="centered")
st.title("📄 Multi-Doc Deep Summarizer")

uploaded_files = st.file_uploader(
    "Upload PDF, DOCX, TXT, or Excel files",
    type=["pdf", "docx", "txt", "xlsx"],
    accept_multiple_files=True
)

if uploaded_files:
    st.info("✅ Files uploaded. Ready to summarize.")
    file_data = []

    for uploaded_file in uploaded_files:
        suffix = uploaded_file.name.split(".")[-1]
        file_type = suffix.lower()

        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_type}") as tmp:
            tmp.write(uploaded_file.read())
            file_data.append((tmp.name, file_type))

    if st.button("🔍 Generate Summary"):
        try:
            st.write("🧠 Creating vectorstore...")
            vectorstore = get_vectorstore(file_data)

            st.write("📄 Generating deep summary...")
            summary = get_deep_summary(vectorstore)

            st.subheader("📌 Deep Summary")
            st.write(summary)

            st.download_button(
                label="📥 Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"❌ Error: {e}")
