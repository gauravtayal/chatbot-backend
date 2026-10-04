from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

from app.core.config import settings


embeddings = OllamaEmbeddings(model="nomic-embed-text",temperature=0)

def get_hr_vector_store():

    vector_store = Chroma(
        collection_name="hr_documents",
        embedding_function=embeddings,
        persist_directory="./chromaDB"
    )

    return vector_store