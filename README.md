# LLM-Server

This project provides a simple FastAPI web server that simulates responses from a language model (LLM).  
It includes structured API endpoints, input validation, automated testing, linting, and formatting.


## Features

- POST /v1/generate: Accepts a user prompt and returns a simulated LLM response.
- Input validation: Empty, unsafe, or excessively long prompts are rejected.
- Pre-push Git hook to ensure:
  - All tests pass (pytest)
  - Type checks succeed (mypy)
  - Code style is clean (flake8)
  - Code is properly formatted (black --check)

## Installation

1. Clone the repository:
git clone https://github.com/NoyushG/LLMPythonProject.git
cd LLMPythonProject
2. Install dependencies:
pip install -r requirements.txt
3. Run main.py to activate the server
