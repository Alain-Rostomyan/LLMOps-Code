# app/services/ollama_service.py

from app.services.base import LLMService
from typing import List, Dict
import httpx

OLLAMA_BASE_URL = "http://localhost:11434/api/chat"

class OllamaService(LLMService):
    async def generate(self, messages: List[Dict[str, str]]) -> str:
        payload = {
            "model": "llama3",  # or "mistral", etc.
            "messages": messages,
            "stream": False
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(OLLAMA_BASE_URL, json=payload)
            response.raise_for_status()
            result = response.json()
            return result["message"]["content"]
