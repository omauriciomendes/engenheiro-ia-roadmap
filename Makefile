.PHONY: setup test run api lint format

setup:
	python -m venv .venv && . .venv/bin/activate && pip install -U pip && pip install -r requirements.txt

test:
	pytest -q

lint:
	ruff check src

format:
	ruff format src

api:
	uvicorn src.api.app:app --reload --port 8000