"""Pydantic models used by the product API."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, HttpUrl


class Product(BaseModel):
    """Schema describing a product in the catalogue."""

    id: int
    name: str
    description: str
    price: float
    category: str
    image_url: Optional[HttpUrl]
