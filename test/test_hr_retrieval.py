import sys
from pathlib import Path
import asyncio


ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.chatbots.hr.retriever import (
    get_hr_retriever
)


async def test_retrieval():

    retriever = get_hr_retriever()

    documents = await retriever.ainvoke(
        "What is the maternity leave policy?"
    )

    for document in documents:

        print("\n----------------")

        print(
            document.page_content
        )

        print(
            document.metadata
        )


if __name__ == "__main__":

    asyncio.run(
        test_retrieval()
    )