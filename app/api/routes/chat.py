from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.conversation_service import get_conversation, add_message_to_conversation
from app.services.llm_service import generate_response

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    add_message_to_conversation(request.session_id, "user", request.message)

    conversation = get_conversation(request.session_id)
    answer = generate_response(conversation)

    add_message_to_conversation(request.session_id, "assistant", answer)

    return ChatResponse(session_id=request.session_id, answer=answer)