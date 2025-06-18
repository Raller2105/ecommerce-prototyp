from faker import Faker
import json
import random

fake = Faker()

def generate_product():
    return {
        "name": fake.catch_phrase(),
        "description": fake.text(max_nb_chars=200),
        "price": round(random.uniform(5, 500), 2),
        "category": random.choice(["Elektronik", "Haushalt", "Mode", "Bücher", "Sport"]),
        "image_url": fake.image_url()
    }

products = [generate_product() for _ in range(1000)]

with open("data/products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print("✅ 1000 Produkt-Datensätze generiert.")
