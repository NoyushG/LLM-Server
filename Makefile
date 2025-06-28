# Makefile for FastAPI project with testing, linting, and type checking

# Default target - shows available commands
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make test         - run all tests with pytest"
	@echo "  make lint         - run flake8 to check code style"
	@echo "  make typecheck    - run mypy for type checking"
	@echo "  make format       - run black to auto-format the code"
	@echo "  make format-check - check code formatting with black"
	@echo "  make check        - run all checks (test, lint, typecheck, format-check)"
	@echo "  make run          - run FastAPI server locally with reload"

# Run tests with pytest
.PHONY: test
test:
	pytest tests/

# Run flake8 for linting on app and tests directories
.PHONY: lint
lint:
	flake8 app tests

# Run mypy type checker on app directory
.PHONY: typecheck
typecheck:
	mypy app

# Format code with black on app and tests directories
.PHONY: format
format:
	black app tests

# Check code formatting with black without making changes
.PHONY: format-check
format-check:
	black --check app tests

# Run all checks together
.PHONY: check
check: test lint typecheck format-check

# Run FastAPI server with auto-reload for development
.PHONY: run
run:
	uvicorn app.main:app --reload --host localhost --port 8000
