"""API routes that expose the product catalogue."""
from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from ...models.product import Product
from ...services.catalogue import CatalogueService, get_catalogue_service

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=List[Product])
def list_products(catalogue: CatalogueService = Depends(get_catalogue_service)) -> List[Product]:
    """Return all products."""

    return catalogue.list_products()


@router.get("/{product_id}", response_model=Product)
def get_product(
    product_id: int,
    catalogue: CatalogueService = Depends(get_catalogue_service),
) -> Product:
    """Return a single product by its identifier."""

    product = catalogue.get_product(product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {product_id} not found.",
        )
    return product
