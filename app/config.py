from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_name: str = "t5-small"
    max_length_default: int = 100
    min_length_default: int = 10

    class Config:
        env_file = ".env"
settings = Settings()
