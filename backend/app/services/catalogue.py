"""Utilities to work with the product catalogue."""
from __future__ import annotations

from typing import List, Optional

from ..core.config import get_settings
from ..models.product import Product


class CatalogueService:
    """Provide access to the static product catalogue."""

    def __init__(self) -> None:
        settings = get_settings()
        raw_products = settings.product_data()
        self._products: List[Product] = [
            Product(id=index, **product) for index, product in enumerate(raw_products, start=1)
        ]

    def list_products(self) -> List[Product]:
        """Return all products."""

        return list(self._products)

    def get_product(self, product_id: int) -> Optional[Product]:
        """Return a single product by id or ``None`` if not found."""

        return next((p for p in self._products if p.id == product_id), None)


def get_catalogue_service() -> CatalogueService:
    """Return a catalogue service instance.

    ``CatalogueService`` has no state that changes at runtime, so returning
    the same instance on each dependency injection call is safe and improves
    performance by avoiding repeated JSON parsing.
    """

    if not hasattr(get_catalogue_service, "_instance"):
        get_catalogue_service._instance = CatalogueService()  # type: ignore[attr-defined]
    return get_catalogue_service._instance  # type: ignore[attr-defined]
