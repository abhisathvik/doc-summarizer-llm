from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import pipeline
from utils import load_documents

def get_vectorstore(files):
    all_docs = []

    for file_path, file_type in files:
        try:
            docs = load_documents(file_path, file_type)
            print(f"✅ Loaded {len(docs)} docs from {file_path}")
            all_docs.extend(docs)
        except Exception as e:
            print(f"❌ Failed loading {file_path} ({file_type}): {e}")

    if not all_docs:
        raise ValueError("❌ No documents loaded. Check file types or contents.")

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(all_docs)

    print(f"🔹 Total Chunks: {len(chunks)}")
    if not chunks:
        raise ValueError("❌ No content to process after chunking.")

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L3-v2")
    return FAISS.from_documents(chunks, embeddings)

def get_deep_summary(vectorstore):
    docs = vectorstore.similarity_search("summarize", k=6)

    if not docs:
        return "⚠️ No content found for summarization."

    content = "\n\n".join([doc.page_content for doc in docs])
    if len(content.strip()) < 100:
        return "⚠️ Content too short for meaningful summarization."

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    try:
        summary = summarizer(content, max_length=700, min_length=200, do_sample=False)[0]['summary_text']
        return summary
    except Exception as e:
        print("❌ Summarization failed:", e)
        return "❌ An error occurred during summarization."
