import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from store.models import Product

products = [
    {
        "name": "Smart Watch Series X",
        "description": "The latest smartwatch with advanced health tracking and beautiful display.",
        "price": "299.00",
        "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80"
    },
    {
        "name": "Wireless Headphones",
        "description": "Noise-cancelling wireless headphones with incredible battery life.",
        "price": "149.00",
        "image_url": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80"
    },
    {
        "name": "Minimal Desk Setup",
        "description": "A refined collection of desk accessories designed for the modern aesthetic.",
        "price": "89.00",
        "image_url": "https://images.unsplash.com/photo-1585386959984-a4155224a1ad?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80"
    },
    {
        "name": "Mechanical Keyboard",
        "description": "Tactile switch mechanical keyboard with customizable RGB.",
        "price": "129.00",
        "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80"
    }
]

def run():
    Product.objects.all().delete()
    for p in products:
        Product.objects.create(**p)
    print("Database seeded with mock products.")

if __name__ == '__main__':
    run()
