from app.services.openai_service import OpenAIService
from app.services.ollama_service import OllamaService
from app.services.base import LLMService

def get_llm_service(provider: str) -> LLMService:
    if provider == "openai":
        return OpenAIService()
    elif provider == "ollama":
        return OllamaService()
    else:
        raise ValueError(f"Unsupported provider: {provider}")
