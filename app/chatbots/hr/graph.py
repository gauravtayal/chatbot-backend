from langgraph.graph import StateGraph,START,END
from contextlib import asynccontextmanager

from app.chatbots.hr.nodes import retrieve_documents, generate_answer,rewrite_question
from app.chatbots.hr.states import HRState

from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver


builder = StateGraph(HRState)

builder.add_node("rewrite", rewrite_question)
builder.add_node("retrieve", retrieve_documents)
builder.add_node("generate", generate_answer)
builder.add_edge(START, "rewrite")
builder.add_edge("rewrite", "retrieve")
builder.add_edge("retrieve", "generate")

builder.add_edge("generate", END)

@asynccontextmanager
async def create_hr_graph():
    async with AsyncSqliteSaver.from_conn_string("chatbot_memory.db") as checkpointer:
        yield builder.compile(checkpointer=checkpointer)
