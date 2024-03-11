from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_PATH: str

    class Config:
        env_file = "./src/.env"

    @property
    def DATABASE_URL(self):
        # sqlite+aiosqlite:///file_path
        return f"sqlite+aiosqlite:///{self.DB_PATH}"


settings = Settings()
