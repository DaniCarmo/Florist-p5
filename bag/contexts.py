from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                if size:
                    if size == 'l':
                        total += quantity * product.price_l
                        price = float(product.price_l)
                    elif size == 'm':
                        total += quantity * product.price_m
                        price = float(product.price_m)
                    elif size == 's':
                        total += quantity * product.price_s
                        price = float(product.price_s)
                    else:
                        total += quantity * product.price
                        price = float(product.price)
                else:
                    total += quantity * product.price
                    price = float(product.price)
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'price':price
                })

    # Check if the user is logged in
    if request.user.is_authenticated:
        # If logged in, set delivery fee to zero for free shipping
        delivery = 0
    else:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context