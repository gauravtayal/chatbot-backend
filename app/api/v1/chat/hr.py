from collections.abc import AsyncGenerator
from copy import error

from fastapi import APIRouter, Request

from fastapi.responses import StreamingResponse

from app.services.streaming import create_stream_event


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

@router.post("/stream")
async def chat_stream(request: Request, body: ChatRequest):

    graph = request.app.state.hr_graph

    config = {
        "configurable": {
            "thread_id": body.session_id
        }
    }

    async def generate() -> AsyncGenerator[str, None]:

        try:

            async for chunk, metadata in graph.astream(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": body.message
                        }
                    ]
                },
                config=config,
                stream_mode="messages"
            ):

                if chunk.content:

                    yield create_stream_event(
                        "token",
                        chunk.content
                    )

            yield create_stream_event(
                "done"
            )

        except Exception as error:

            yield create_stream_event(
                "error",
                str(error)
            )

    return StreamingResponse(
        generate(),
        media_type="application/x-ndjson"
    )


@router.get("/history/{session_id}")
async def get_history(
    request: Request,
    session_id: str
):

    graph = request.app.state.hr_graph

    config = {
        "configurable": {
            "thread_id": session_id
        }
    }

    state = await graph.aget_state(
        config
    )

    messages = state.values.get(
        "messages",
        []
    )

    return {
        "session_id": session_id,
        "messages": [
            {
                "role": message.type,
                "content": message.content
            }
            for message in messages
        ]
    }