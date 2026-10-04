from multiprocessing.dummy import connection

import aiosqlite

from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver


async def create_checkpointer():

    checkpointer  = AsyncSqliteSaver.from_conn_string("chatbot_memory.db")

    return checkpointer 