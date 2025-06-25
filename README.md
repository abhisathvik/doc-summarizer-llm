# 📄 SmartDoc Summarizer

**SmartDoc Summarizer** is a powerful Streamlit-based web app that allows users to upload documents (PDF, DOCX, TXT, XLSX) and receive a detailed, multi-paragraph AI-generated summary using Hugging Face language models and LangChain.

---

## 🚀 Features

✅ Upload multiple documents  
✅ Supported formats: **PDF**, **TXT**, **DOCX**, **Excel (.xlsx)**  
✅ Uses **deep summarization** powered by `facebook/bart-large-cnn`  
✅ Utilizes **semantic embeddings** for document understanding  
✅ Clean, responsive **Streamlit UI**  
✅ Downloadable summary as `.txt` file  
✅ 100% Local using Hugging Face — **no OpenAI required**

---

## 🧰 Tech Stack

- [Streamlit](https://streamlit.io) — Web UI framework
- [HuggingFace Transformers](https://huggingface.co/transformers) — For summarization
- [Sentence Transformers](https://www.sbert.net) — For vector embeddings
- [LangChain](https://www.langchain.com) — For document chunking & retrieval
- `docx2txt`, `openpyxl`, `unstructured` — File parsing

---

## 📂 Project Structure

doc-summarizer-llm/

│
├── app.py                     # Streamlit UI
├── pdf_qa.py                  # Core LangChain logic
├── utils.py                   # PDF loading & chunking
├── .env                       # API keys
├── requirements.txt           # For deployment
└── README.md

# Installing the necessary libraries

- pip install langchain openai faiss-cpu pypdf python-dotenv streamlit

- pip install tiktoken

- pip install openai faiss-cpu python-dotenv pypdf

- pip install -U langchain langchain-community langchain-openai

- pip install sentence-transformers langchainhub

- pip install transformers

- pip install accelerate

- pip install streamlit python-docx openpyxl

- pip install docx2txt

- pip install torch

- pip install unstructured openpyxl

- pip freeze > requirements.txt

# Run the APP

- streamlit run app.py

# 🛡️ License

MIT License. Feel free to use, modify, and contribute.

# 🙌 Acknowledgements
Thanks to:
 - HuggingFace
 - LangChain
 - Streamlit

# ✨ Contact
Built by Abhi Sathvik Reddy

GitHub: @abhisathvik

LinkedIn: https://www.linkedin.com/in/abhi-sathvik-reddy-aniga-a7b15b256/
