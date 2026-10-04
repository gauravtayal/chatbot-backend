from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    session_id: str

class chatResponse(BaseModel):
    answer: str
    session_id: str
    
        