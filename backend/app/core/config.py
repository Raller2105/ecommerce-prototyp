"""Application configuration utilities."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import List

from pydantic import BaseSettings, Field

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_DATA_FILE = PROJECT_ROOT / "data" / "products.json"


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    data_file: Path = Field(
        default=DEFAULT_DATA_FILE,
        description="Path to the product catalogue JSON file.",
    )

    class Config:
        env_prefix = "ECOMMERCE_"
        env_file = ".env"
        env_file_encoding = "utf-8"

    def product_data(self) -> List[dict]:
        """Load and return the product catalogue as a list of dicts."""
        data_path = self.data_file
        if not data_path.is_file():
            raise FileNotFoundError(
                f"Product data file not found: {data_path.resolve()}"
            )
        import json

        with data_path.open("r", encoding="utf-8") as fp:
            return json.load(fp)


@lru_cache()
def get_settings() -> Settings:
    """Return a cached ``Settings`` instance."""

    return Settings()
