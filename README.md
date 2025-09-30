# 🛒 E-Commerce-Prototyp – Abschlussprojekt (Techstarter)

Dieses Projekt ist Teil meines Techstarter-Kurses. Ziel ist ein skalierbarer Onlineshop mit:

- ✅ React-Frontend (Produktanzeige, Warenkorb, Checkout)
- ✅ Python-Backend (API mit FastAPI)
- ✅ PostgreSQL-Datenbank mit >100.000 Faker-Datensätzen
- ✅ CI/CD für Frontend, Backend und Infrastruktur
- ✅ AWS Deployment über Terraform & Ansible
- ✅ Umsetzung in 2–3 Sprints nach Scrum

---

## 📁 Projektstruktur

```plaintext
frontend/   → React-Anwendung
backend/    → Python-Backend mit FastAPI
infra/      → Terraform & Ansible Deployment
ci/         → GitHub Actions für Build/Deployment
data/       → Faker-Daten-Generator
docs/       → User Stories, Sprint-Dokumentation
```

> ⚠️ Viele Bereiche befinden sich noch in Arbeit. Nach und nach werden die einzelnen Komponenten ausgebaut.

---

## 🚀 Aktueller Stand Backend

Der erste Meilenstein ist eine FastAPI-Anwendung, die die Produktdaten aus `data/products.json` einliest und über Endpunkte bereitstellt.

### Endpunkte

| Methode | Pfad | Beschreibung |
|---------|------|--------------|
| `GET` | `/health` | Health-Check der API |
| `GET` | `/products/` | Liste aller Produkte |
| `GET` | `/products/{id}` | Detailansicht eines einzelnen Produkts |

### Schnelles Ausprobieren

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Anschließend ist die API standardmäßig unter `http://127.0.0.1:8000` erreichbar (Swagger UI unter `/docs`).

---

## 🧪 Tests

In `backend/tests` befindet sich eine kleine Test-Suite auf Basis von `pytest`, die die wichtigsten Endpunkte überprüft:

```bash
cd backend
pytest
```

---

## 🗂️ Daten

Im Ordner `data/` liegt ein Generator (`generate_fake_data.py`), der mithilfe von Faker Produktdatensätze erzeugt und in `products.json` speichert. Diese Datei dient aktuell sowohl dem Backend als auch künftigen Frontend-Mockups als Datenbasis.

---

## ✅ Nächste Schritte

- Aufbau des React-Frontends und Integration mit der API
- Vorbereitung einer PostgreSQL-Datenbank inkl. Migrationsskripten
- Automatisierte Tests & Linting im CI
- Infrastruktur-Code für das Cloud-Deployment
