# app/services/openai_service.py

import httpx
import os
from typing import List, Dict
from app.services.base import LLMService

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key-here")
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

class OpenAIService(LLMService):
    async def generate(self, messages: List[Dict[str, str]]) -> str:
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": messages,
            "temperature": 0.7,
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(OPENAI_API_URL, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"]
