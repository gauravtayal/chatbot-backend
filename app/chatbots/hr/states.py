from typing import Annotated, TypedDict

from langgraph.graph import add_messages


class HRState(TypedDict):

    messages: Annotated[list, add_messages]

    question: str

    search_query: str

    context: str

    answer: str

    chat_history: list
