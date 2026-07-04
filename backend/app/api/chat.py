from fastapi import APIRouter

from app.schemas.chat import ChatRequest
from app.schemas.chat import ChatResponse

from app.services.chat_service import ask_question

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    result = ask_question(request.question)

    return ChatResponse(

        answer=result["answer"],

        sources=result["sources"]

    )