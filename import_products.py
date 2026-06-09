import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product


products = [

    # Phones
    ("iQOO Neo 10", 34999, "Powerful gaming smartphone with Snapdragon processor", "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9", "Phone"),
    ("iPhone 16 Pro Max", 149999, "Apple flagship smartphone", "https://images.unsplash.com/photo-1512496015851-a90fb38ba796", "Phone"),
    ("Samsung Galaxy S25 Ultra", 129999, "Premium Samsung smartphone", "https://images.unsplash.com/photo-1598327105666-5b89351aff97", "Phone"),
    ("OnePlus 13", 69999, "Fast and smooth flagship phone", "https://images.unsplash.com/photo-1580910051074-3eb694886505", "Phone"),

    # Laptops
    ("MacBook Air M4", 119999, "Apple M4 ultra-efficient laptop", "https://images.unsplash.com/photo-1517336714739-489689fd1ca8", "Laptop"),
    ("ASUS ROG Strix G16", 139999, "High-end gaming laptop", "https://images.unsplash.com/photo-1496181133206-80ce9b88a853", "Laptop"),
    ("Dell XPS 15", 129999, "Premium productivity laptop", "https://images.unsplash.com/photo-1484788984921-03950022c9ef", "Laptop"),

    # Headphones
    ("Sony WH-1000XM5", 29999, "Industry-leading noise cancellation", "https://images.unsplash.com/photo-1505740420928-5e560c06d30e", "Headphone"),
    ("Boat Rockerz 550", 1999, "Affordable wireless headphones", "https://images.unsplash.com/photo-1484704849700-f032a568e944", "Headphone"),
    ("JBL Tune 770NC", 8999, "Wireless ANC headphones", "https://images.unsplash.com/photo-1505740420928-5e560c06d30e", "Headphone"),

    # Watches
    ("Apple Watch Series 10", 49999, "Advanced smartwatch", "https://images.unsplash.com/photo-1523275335684-37898b6baf30", "Watch"),
    ("Samsung Galaxy Watch 8", 32999, "Premium Android smartwatch", "https://images.unsplash.com/photo-1546868871-7041f2a55e12", "Watch"),
]

for p in products:
    Product.objects.create(
        name=p[0],
        price=p[1],
        description=p[2],
        image=p[3],
        category=p[4]
    )

print("Tech products imported successfully!")