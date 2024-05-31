import json
from products.models import Product

def load_products_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        for item in data:
            fields = item['fields']
            if isinstance(fields['price'], dict):
                price_s = fields['price'].get('s')
                price_m = fields['price'].get('m')
                price_l = fields['price'].get('l')
                price = None
                has_sizes = True
            else:
                price_s = None
                price_m = None
                price_l = None
                price = fields['price']
                has_sizes = False

            Product.objects.create(
                pk=item['pk'],
                sku=fields['sku'],
                name=fields['name'],
                description=fields['description'],
                price=price,
                price_s=price_s,
                price_m=price_m,
                price_l=price_l,
                category_id=fields['category'],
                rating=fields['rating'],
                image_url=fields['image_url'],
                image=fields['image'],
                has_sizes=has_sizes
            )