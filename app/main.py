
from fastapi import FastAPI

from app.api.routes.chat import router as chat_router

app = FastAPI(title="AI Assistant API", version="1.0.0")

app.include_router(chat_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}        
