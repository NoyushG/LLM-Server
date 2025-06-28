"""
API router for version 1 of the LLM Service.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    response: str

@router.get("/")
def root():
    """
    Welcome message for root endpoint
    """
    return {"message": "Welcome to LLM Service!"}


@router.post("/generate", response_model=PromptResponse)
def generate_response(prompt: PromptRequest) -> PromptResponse:
    """
    Accepts a prompt and returns a response from the simulated LLM.

    Args:
        prompt (PromptRequest): The user's prompt.

    Returns:
        PromptResponse: The generated response.
    """

    response = llm(prompt.prompt)
    return PromptResponse(response=response)


def validate_prompt(prompt: str) -> None:
    """
    Validates the provided prompt to ensure it is safe and acceptable for processing.

    Args:
        prompt (str): The input prompt provided by the user.

    Raises:
        HTTPException: If the prompt fails any of the validation rules.
    """

    # Avoid empty prompts.
    if not prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")

    # Avoid enormous prompts.
    if len(prompt) > 1000:
        raise HTTPException(status_code=400, detail="Prompt is too long")

    # Avoid dangerous prompts.
    if any(x in prompt.lower() for x in ["<script>", "drop table", "ignore previous"]):
        raise HTTPException(status_code=400, detail="Prompt contains unsafe content")


def llm(prompt: str) -> str:
    """
    Simulates a response from a large language model (LLM).

    Args:
        prompt (str): The input prompt from the user.

    Returns:
        str: The simulated response.
    """

    validate_prompt(prompt)
    return "LLM's Answer"
