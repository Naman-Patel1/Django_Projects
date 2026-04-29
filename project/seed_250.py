import os
import django
import json
import urllib.request

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from store.models import Product

def fetch_and_seed_products():
    print("Clearing old products...")
    Product.objects.all().delete()
    
    print("Fetching authentic dummy product data from an external API...")
    try:
        url = "https://dummyjson.com/products?limit=250"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req).read()
        data = json.loads(response.decode('utf-8'))
        
        items = data.get('products', [])
        
        products_to_create = []
        for item in items:
            image_url = ''
            if item.get('images') and len(item['images']) > 0:
                image_url = item['images'][0]
            elif item.get('thumbnail'):
                image_url = item['thumbnail']
                
            products_to_create.append(
                Product(
                    name=item.get('title', 'Unknown Product'),
                    description=item.get('description', ''),
                    price=item.get('price', 0.0),
                    image_url=image_url
                )
            )
            
        Product.objects.bulk_create(products_to_create)
        print(f"Successfully seeded {len(products_to_create)} fully authentic products!")

    except Exception as e:
        print(f"Failed to fetch or seed items: {e}")

if __name__ == '__main__':
    fetch_and_seed_products()
