from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


@dataclass(slots=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "SceneSound OS")
    app_env: str = os.getenv("APP_ENV", "development")
    secret_key: str = os.getenv("SECRET_KEY", "development-secret-key")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./data/scenesound.db")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    @property
    def database_path(self) -> Path:
        if self.database_url.startswith("sqlite:///./"):
            relative_path = self.database_url.replace("sqlite:///./", "", 1)
            return BASE_DIR / relative_path
        if self.database_url.startswith("sqlite:////"):
            return Path(self.database_url.replace("sqlite:///", "", 1))
        return BASE_DIR / "data" / "scenesound.db"


settings = Settings()
