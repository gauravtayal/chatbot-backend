from pathlib import Path
import sys

from langchain_text_splitters import RecursiveCharacterTextSplitter

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from ingestion.pdf_loader import load_pdf
from app.services.vector_services import get_hr_vector_store



HR_DATA_PATH = Path("./data/hr")


def load_hr_documents():

    documents = []

    for pdf_file in HR_DATA_PATH.glob("*.pdf"):

        print(f"Loading: {pdf_file}")

        pdf_documents = load_pdf(
            str(pdf_file)
        )

        documents.extend(pdf_documents)

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(
        documents
    )

    return chunks

def ingest():

    documents = load_hr_documents()

    print(
        f"Loaded {len(documents)} pages"
    )

    chunks = split_documents(
        documents
    )

    print(
        f"Created {len(chunks)} chunks"
    )

    vector_store = get_hr_vector_store()

    vector_store.add_documents(
        documents=chunks
    )

    print(
        "HR documents successfully stored!"
    )



if __name__ == "__main__":

 ingest()
