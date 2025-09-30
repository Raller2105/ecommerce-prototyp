# Backend – FastAPI Produktkatalog

Dieser Ordner enthält einen ersten Prototypen des Python-Backends auf Basis von [FastAPI](https://fastapi.tiangolo.com/). Die API lädt die Produktdaten aus `data/products.json` und stellt sie über einfache Endpunkte zur Verfügung.

## Voraussetzungen

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

## Entwicklung starten

```bash
uvicorn app.main:app --reload
```

## Tests ausführen

```bash
pytest
```

## Konfiguration

Die Anwendung kann über Umgebungsvariablen konfiguriert werden. Alle Variablen verwenden den Präfix `ECOMMERCE_`.

| Variable | Beschreibung | Standardwert |
|----------|--------------|--------------|
| `ECOMMERCE_DATA_FILE` | Pfad zur JSON-Datei mit den Produktdaten | `data/products.json` |

Alternativ kann eine `.env`-Datei im Projektverzeichnis genutzt werden.
