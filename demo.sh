#!/bin/bash
export $(cat .env | xargs)
uvicorn src.api.app:app --reload --host 0.0.0.0 --port ${APP_PORT:-8000}
