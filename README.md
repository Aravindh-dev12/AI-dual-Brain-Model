# Dual-Brain AI — Strong MVP

Production-oriented MVP for the Dual-Brain AI architecture (Main Brain + Specialist Brain).
This repo uses FastAPI, structured config, CI, tests, and an intelligent fusion layer.

Quickstart (local):
1. Copy `.env.example` to `.env` and populate API keys.
OPENAI_API_KEY=
DEEPSEEK_API_KEY=
OPENAI_MODEL=
DEEPSEEK_ENDPOINT=
APP_PORT=8000

2. Create virtualenv and install: `pip install -r requirements.txt`
3. Run app: `uvicorn src.api.app:app --reload --host 0.0.0.0 --port 8000`
4. Open API docs at http://127.0.0.1:8000/docs


