from fastapi import APIRouter

from app.api.v1.chat import hr
# from app.api.v1.chat import ecommerce
# from app.api.v1.chat import support

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(
    hr.router,
    prefix="/chat/hr",
    tags=["HR Chatbot"]
)

# api_router.include_router(
#     ecommerce.router,
#     prefix="/chat/ecommerce",
#     tags=["E-commerce Chatbot"]
# )

# api_router.include_router(
#     support.router,
#     prefix="/chat/support",
#     tags=["Support Chatbot"]
# )