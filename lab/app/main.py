# app/main.py

from fastapi import FastAPI
from app.api import router

app = FastAPI(title="LLM Gateway API")

# Include the main router
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the LLM Gateway API"}
