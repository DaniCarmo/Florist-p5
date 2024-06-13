from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from .forms import WishlistForm
from products.models import Product

@login_required
def wishlist_list(request):
    wishlists = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist_list.html', {'wishlists': wishlists})

@login_required
def wishlist_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            wishlist_item = form.save(commit=False)
            wishlist_item.user = request.user
            wishlist_item.product = product
            wishlist_item.save()
            return redirect('wishlist_list')
    else:
        form = WishlistForm()

    return render(request, 'wishlist_form.html', {'form': form})

@login_required
def wishlist_edit(request, id):
    wishlist_item = get_object_or_404(Wishlist, id=id, user=request.user)
    if request.method == 'POST':
        form = WishlistForm(request.POST, instance=wishlist_item)
        if form.is_valid():
            form.save()
            return redirect('wishlist_list')
    else:
        form = WishlistForm(instance=wishlist_item)
    return render(request, 'wishlist_form.html', {'form': form})

@login_required
def wishlist_delete(request, id):
    wishlist_item = get_object_or_404(Wishlist, id=id, user=request.user)
    if request.method == 'POST':
        wishlist_item.delete()
        return redirect('wishlist_list')
    return render(request, 'wishlist_confirm_delete.html', {'wishlist_item': wishlist_item})