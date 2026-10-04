# Chatbot Backend

FastAPI backend for an AI chatbot platform. The current implementation exposes an HR chatbot that answers questions from HR policy PDFs using a RAG pipeline with LangGraph, LangChain, Chroma, and Ollama.

## What It Does

- Loads HR PDF documents from `data/hr`
- Splits documents into searchable chunks
- Stores embeddings in a local Chroma vector database
- Retrieves relevant HR policy context for each user question
- Uses a LangGraph workflow to rewrite, retrieve, and answer questions
- Persists chat memory with a SQLite LangGraph checkpointer
- Serves the chatbot through a FastAPI endpoint

The ecommerce and support chatbot routes are scaffolded but not enabled yet.

## Project Structure

```text
app/
  api/v1/             FastAPI routers and chat endpoints
  chatbots/hr/        HR chatbot graph, nodes, prompts, state, retriever
  core/               App configuration
  schemas/            Request and response models
  services/           LLM, vector store, and checkpointer services
data/
  hr/                 HR source PDFs
  ecommerce/          Ecommerce source PDFs
  support/            Support source PDFs
ingestion/
  ingest_hr.py        Builds the HR Chroma collection from PDFs
  pdf_loader.py       PDF loading helper
test/
  test_hr_retrieval.py Manual retrieval smoke test
```

## Requirements

- Python `>=3.14`
- `uv`
- Ollama running locally
- Ollama models:
  - `llama3.2`
  - `nomic-embed-text`

Pull the models with:

```powershell
ollama pull llama3.2
ollama pull nomic-embed-text
```

## Setup

Install dependencies:

```powershell
uv sync
```

Create a `.env` file if needed. The app currently supports:

```env
CHROMA_PATH=./chromaDB
```

## Ingest HR Documents

Before using the HR chatbot, build the vector database:

```powershell
.\.venv\Scripts\python.exe ingestion\ingest_hr.py
```

This reads PDFs from `data/hr` and writes embeddings to `./chromaDB`.

## Run The API

```powershell
.\.venv\Scripts\fastapi.exe dev app\main.py
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive docs:

```text
http://127.0.0.1:8000/docs
```

## HR Chat Endpoint

```http
POST /api/v1/chat/hr
```

Request body:

```json
{
  "message": "What is the maternity leave policy?",
  "session_id": "user-123"
}
```

Response body:

```json
{
  "answer": "Answer generated from the HR knowledge base.",
  "session_id": "user-123"
}
```

## Manual Retrieval Test

To verify that HR retrieval is working:

```powershell
.\.venv\Scripts\python.exe test\test_hr_retrieval.py
```

## Notes

- Chroma data is stored locally in `chromaDB`.
- LangGraph conversation checkpoints are stored in `chatbot_memory.db`.
- The enabled route is currently only the HR chatbot: `/api/v1/chat/hr`.
- Ecommerce and support datasets exist under `data/`, but their routers are commented out.
