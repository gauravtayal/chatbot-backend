from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    chroma_path: str = "./chromaDB"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()      
