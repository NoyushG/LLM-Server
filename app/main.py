"""
Main entry point for the FastAPI application.
"""

from fastapi import FastAPI
from app.api import router

PORT = 8000
HOST = "localhost"

app = FastAPI(
    title="LLM Service",
    version="1.0.0",
    description="A simulated LLM service that responds to prompts as if it were a real language model.",
)

app.include_router(router, prefix="/v1")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)
