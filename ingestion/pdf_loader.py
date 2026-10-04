from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path: str):
    """
    Load a PDF file and return its content as a list of documents.
    """
    path = Path(file_path)
    if not path.exists() or path.suffix.lower() != ".pdf":
        raise FileNotFoundError(f"File not found or invalid format: {file_path}")
    
    loader = PyPDFLoader(str(path))
    documents = loader.load()
    return documents