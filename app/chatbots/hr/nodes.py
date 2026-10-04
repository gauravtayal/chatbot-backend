from app.chatbots.hr.states import HRState

from app.chatbots.hr.retriever import (
    get_hr_retriever
)

from app.services.llm_services import model

from app.chatbots.hr.prompts import (
    HR_SYSTEM_PROMPT
)


retriever = get_hr_retriever()


async def rewrite_question(
    state: HRState
):

    messages = state["messages"]

    question = messages[-1].content

    prompt = f"""
You are an HR search query optimizer.

Conversation:

{messages}

User's latest question:

{question}

Convert the latest question into a standalone
search query for an HR policy knowledge base.

If the question is already standalone,
return it unchanged.

Return ONLY the search query.
"""

    response = await model.ainvoke(prompt)

    return {
        "search_query": response.content.strip()
    }


async def retrieve_documents(
    state: HRState
):

    search_query = state["search_query"]

    documents = await retriever.ainvoke(
        search_query
    )

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    return {
        "context": context
    }


async def generate_answer(
    state: HRState
):

    messages = state["messages"]

    question = messages[-1].content

    context = state["context"]

    prompt = HR_SYSTEM_PROMPT.format(
        question=question,
        context=context
    )

    response = await model.ainvoke(
        prompt
    )

    answer = response.content

    return {
        "answer": answer,
        "messages": [
            {
                "role": "assistant",
                "content": answer
            }
        ]
    }
