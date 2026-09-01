from dotenv import load_dotenv
from openai import OpenAI
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()
client = OpenAI()
app = FastAPI()

try:
    class ChatRequest(BaseModel):
        session_id: str
        message: str

    class ChatResponse(BaseModel):
        session_id: str
        answer: str

    conversations = {}

    @app.get("/")
    def home():
        return {"message": "Welcome to the AI Assistant API. Use the /ask endpoint to interact with the assistant."}

    @app.post("/chat", response_model=ChatResponse)
    def ask(request: ChatRequest):

        if request.session_id not in conversations:
            conversations[request.session_id] = []

        conversation = conversations[request.session_id]

        conversation.append({"role": "user", "content": request.message})

        MAX_MESSAGES = 10
        if len(conversation) > MAX_MESSAGES:
            del conversation[:-MAX_MESSAGES:]

        response = client.responses.create(
            instructions="""
            You are a helpful software engineering assistant.
            Answer clearly and concisely.
            """,
            model="gpt-4o-mini",
            input=conversation
        )
        assistant_response = response.output_text
        conversation.append({"role": "assistant", "content": assistant_response})

        return ChatResponse(session_id=request.session_id, answer=assistant_response)
except Exception as e:
    print(f"An error occurred while setting up the API: {e}")