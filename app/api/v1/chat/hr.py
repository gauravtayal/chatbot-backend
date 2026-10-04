from fastapi import APIRouter, Request

from app.schemas.chat import ChatRequest, chatResponse

router = APIRouter()




@router.post("", response_model=chatResponse)
async def chat(request: Request,body:ChatRequest):

    graph = request.app.state.hr_graph

    config = {
        "configurable": {
            "thread_id": body.session_id
        }
    }



    result = await graph.ainvoke({"messages": [{"role": "user", "content": body.message}]}, config=config)

    return chatResponse(answer=result["answer"],session_id=body.session_id)

    
