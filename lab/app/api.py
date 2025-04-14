# app/api.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Literal
from app.services.provider_factory import get_llm_service

router = APIRouter()

class Message(BaseModel):
    role: Literal["user", "system", "assistant"]
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    provider: Literal["openai", "ollama"]

@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        llm = get_llm_service(request.provider)
        response = await llm.generate([msg.dict() for msg in request.messages])
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
