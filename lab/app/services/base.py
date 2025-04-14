# app/services/base.py

from abc import ABC, abstractmethod
from typing import List, Dict, Any

class LLMService(ABC):
    @abstractmethod
    async def generate(self, messages: List[Dict[str, str]]) -> str:
        """
        Takes a list of messages (e.g., from a chat history) and returns the model's response.
        """
        pass
