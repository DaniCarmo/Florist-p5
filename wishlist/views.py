from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decimal import Decimal 
from .models import Wishlist
from products.models import Product


@login_required
def wishlist_list(request):
    wishlists = Wishlist.objects.filter(user=request.user)
    context = {
        'wishlists': wishlists,
    }
    return render(request, 'wishlist/wishlist_list.html', context)

@login_required
def wishlist_to_bag(request, product_id):
    wishlist_item = get_object_or_404(Wishlist, id=product_id, user=request.user)
    product = wishlist_item.product

    # Add the product to the bag
    bag = request.session.get('bag', {})
    price = float(product.price)  # Get the price of the product and convert to float for json

    if product.id in bag:
        bag[product.id]['quantity'] += 1
    else:
        bag[product.id] = {
            'quantity': 1,
            'price': price,  # Add the price to the bag item
        }

    request.session['bag'] = bag

    # Remove item from wishlist
    wishlist_item.delete()

    messages.success(request, f'Added {product.name} to your bag and removed from wishlist')
    return redirect('wishlist_list')

@login_required
def wishlist_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        wishlist_item, created = Wishlist.objects.get_or_create(
            user=request.user,
            product=product,
        )
        if created:
            messages.success(request, 'Product added to wishlist')
        return redirect('product_detail', product_id=product.id)

    return redirect('product_detail', product_id=product.id)

@login_required
def wishlist_delete(request, product_id):
    wishlist_item = get_object_or_404(Wishlist, id=product_id, user=request.user)
    if request.method == 'POST':
        wishlist_item.delete()
        return redirect('wishlist_list')
    
    return render(request, 'wishlist/wishlist_confirm_delete.html', {'wishlist_item': wishlist_item})