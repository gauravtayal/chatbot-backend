from fastapi import FastAPI
from app.api.v1.router import api_router
from app.chatbots.hr.graph import create_hr_graph
from contextlib import asynccontextmanager



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting AI Chatbot Platform...")

    app.state.hr_graph = await create_hr_graph()

    print("HR chatbot graph initialized.")

    yield

    print("Shutting down AI Chatbot Platform...")

app = FastAPI(title="AI chatbot API", version="1.0.0",lifespan=lifespan)

app.include_router(api_router)

@app.get("/")   
async def root():  
    return {"message": "Welcome to the AI chatbot API!"}