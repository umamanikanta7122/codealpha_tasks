import os
import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product

Product.objects.all().delete()

categories = [
    "smartphones",
    "laptops",
    "mobile-accessories"
]

response = requests.get("https://dummyjson.com/products?limit=200")
data = response.json()

for item in data["products"]:
    if item.get("category") in categories:
        Product.objects.create(
            name=item["title"],
            price=item["price"],
            description=item["description"],
            image=item["thumbnail"],
            category=item["category"],
            brand=item.get("brand", "Unknown"),
            rating=item.get("rating", 0),
            stock=item.get("stock", 0)
        )

print("Tech products imported successfully!")
