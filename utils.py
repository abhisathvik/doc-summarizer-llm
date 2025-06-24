from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
    UnstructuredExcelLoader
)

def load_documents(file_path, file_type):
    if file_type == "pdf":
        return PyPDFLoader(file_path).load()
    elif file_type == "txt":
        return TextLoader(file_path).load()
    elif file_type == "docx":
        return Docx2txtLoader(file_path).load()
    elif file_type == "xlsx":
        return UnstructuredExcelLoader(file_path).load()
    else:
        raise ValueError("❌ Unsupported file type")
