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
    wishlist_item = get_object_or_404(Wishlist, id=product_id,
                                      user=request.user)
    product = wishlist_item.product
    # Add the product to the bag
    bag = request.session.get('bag', {})
    price = float(product.price)
    size = wishlist_item.size
    item_id_str = str(product.id)
    quantity = 1
    if size:
        if item_id_str not in bag:
            bag[item_id_str] = {'items_by_size': {}}

        if 'items_by_size' not in bag[item_id_str]:
            bag[item_id_str]['items_by_size'] = {}

        if size in bag[item_id_str]['items_by_size']:
            bag[item_id_str]['items_by_size'][size] += quantity
        else:
            bag[item_id_str]['items_by_size'][size] = quantity

        messages.success(request, f'Added {product.name} '
                         '(size {size}) to your bag')
    else:
        if item_id_str in bag:
            bag[item_id_str] += quantity
            messages.success(request, f'Updated {product.name} '
                             'quantity to {bag[item_id_str]}')
        else:
            bag[item_id_str] = quantity
    request.session['bag'] = bag
    # Remove item from wishlist
    wishlist_item.delete()
    return redirect('wishlist_list')


@login_required
def wishlist_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    size = request.POST.get('product_size')
    if size:
        if size == 'l':
            price = float(product.price_l)
        elif size == 'm':
            price = float(product.price_m)
        elif size == 's':
            price = float(product.price_s)
        else:
            price = float(product.price)
    else:
        price = float(product.price)

    if request.method == 'POST':
        wishlist_item, created = Wishlist.objects.get_or_create(
            user=request.user,
            product=product,
            size=size,
            price=price,
        )
        if created:
            messages.success(request, 'Product added to wishlist')
        else:
            messages.info(request, 'Product already in wishlist')

        # Save the size in the session if provided
        if size:
            wishlist_sizes = request.session.get('wishlist_sizes', {})
            wishlist_sizes[str(product.id)] = size
            request.session['wishlist_sizes'] = wishlist_sizes

        return redirect('product_detail', product_id=product.id)

    return redirect('product_detail', product_id=product.id)


@login_required
def wishlist_delete(request, product_id):
    wishlist_item = get_object_or_404(Wishlist, id=product_id,
                                      user=request.user)

    if request.method == 'POST':
        wishlist_item.delete()
        messages.success(request, 'Product removed from wishlist')
        return redirect('wishlist_list')

    return render(request, 'wishlist/wishlist_confirm_delete.html',
                  {'wishlist_item': wishlist_item})
