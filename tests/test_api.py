"""
Tests for the LLM Service API.
"""

from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)


def test_generate_with_generic_prompt():
    """
    Test that a non-empty prompt returns a response with status 200
    and contains a string.
    """
    payload = {"prompt": "A basic prompt"}
    response = client.post("/v1/generate", json=payload)

    # Should work, legit prompt.
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["response"], str)
    assert len(data["response"]) > 0


@pytest.mark.parametrize("bad_prompt", ["", "   ", "\n\t", "\r\n", " \n "])
def test_generate_empty_prompt(bad_prompt):
    """
    Test that an empty prompt returns a 400 error with appropriate message.
    """
    response = client.post("/v1/generate", json={"prompt": bad_prompt})

    # Should not work, empty prompt.
    assert response.status_code == 400
    assert response.json()["detail"] == "Prompt cannot be empty"
