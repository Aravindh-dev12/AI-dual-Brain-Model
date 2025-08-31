from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API keys and configs
    openai_api_key: str | None = None
    openai_model: str = "gpt-4o-mini"   # default fallback
    deepseek_api_key: str | None = None
    deepseek_endpoint: str | None = None
    app_port: int = 8000

    class Config:
        env_file = ".env"   # load variables from .env in local dev

settings = Settings()
