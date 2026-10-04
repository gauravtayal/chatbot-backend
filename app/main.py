from fastapi import FastAPI
from app.api.v1.router import api_router
from app.chatbots.hr.graph import create_hr_graph
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173",
]



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting AI Chatbot Platform...")

    async with create_hr_graph() as hr_graph:
        app.state.hr_graph = hr_graph

        print("HR chatbot graph initialized.")

        yield

    print("Shutting down AI Chatbot Platform...")

app = FastAPI(title="AI chatbot API", version="1.0.0",lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/")   
async def root():  
    return {"message": "Welcome to the AI chatbot API!"}
