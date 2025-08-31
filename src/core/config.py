from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = None
    openai_model: str = 'gpt-4o-mini'
    deepseek_api_key: str = None
    deepseek_endpoint: str = None
    app_port: int = 8000
    class Config:
        env_file = '.env'

settings = Settings()
