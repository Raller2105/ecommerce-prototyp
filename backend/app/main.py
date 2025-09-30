"""FastAPI application entrypoint for the ecommerce prototype."""
from __future__ import annotations

from fastapi import FastAPI

from .api.routes.products import router as products_router

app = FastAPI(title="E-Commerce Prototype API")


@app.get("/health", tags=["meta"])
def healthcheck() -> dict[str, str]:
    """Simple health check endpoint."""

    return {"status": "ok"}


app.include_router(products_router)
