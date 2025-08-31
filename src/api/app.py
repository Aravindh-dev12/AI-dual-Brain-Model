import os
import uvicorn
from fastapi import FastAPI
from src.core.logging_utils import get_logger
from src.api.routes import router
from src.core.config import settings

logger = get_logger()
app = FastAPI(title="Dual-Brain AI")
app.include_router(router)

@app.on_event("startup")
def startup():
    logger.info("Starting Dual-Brain AI app")
    logger.info(f"App config: model={settings.openai_model}")


# 👇 This is what makes Render detect the port
if __name__ == "__main__":
    uvicorn.run(
        "src.api.app:app",   # 👈 path to your FastAPI `app` object
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),  # Render injects $PORT
        reload=False
    )
