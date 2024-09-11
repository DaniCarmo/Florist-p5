from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """
    bag = request.session.get('bag', {})
    updated_bag = {}
    for item_id, item_data in bag.items():
        try:
            product = get_object_or_404(Product, pk=item_id)
            updated_bag[item_id] = item_data
        except Http404:
            continue  # Skip non-existent products

    request.session['bag'] = updated_bag

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    try:
        product = Product.objects.get(pk=item_id)
    except Product.DoesNotExist:
        messages.error(request, "The product you are trying to add "
                                "does not exist.")
        return redirect(request.POST.get('redirect_url', 'products'))

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = (
        request.POST.get('product_size')
        if 'product_size' in request.POST
        else None
    )
    bag = request.session.get('bag', {})
    item_id_str = str(item_id)

    if size:
        if item_id_str not in bag:
            bag[item_id_str] = {'items_by_size': {}}

        if 'items_by_size' not in bag[item_id_str]:
            bag[item_id_str]['items_by_size'] = {}

        if size in bag[item_id_str]['items_by_size']:
            bag[item_id_str]['items_by_size'][size] += quantity
        else:
            bag[item_id_str]['items_by_size'][size] = quantity

        messages.success(
            request,
            f'Added {product.name} (size {size}) to your bag'
        )
    else:
        if item_id_str in bag:
            bag[item_id_str] += quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id_str]}'
                )
        else:
            bag[item_id_str] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(bag)
    request.session.modified = True  # Ensure the session is saved
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust quantity of the specified product to the specified amount """
    try:
        product = Product.objects.get(pk=item_id)
    except Product.DoesNotExist:
        messages.error(
            request,
            "The product you are trying to adjust does not exist."
            )
        return redirect(reverse('view_bag'))

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)
    messages.success(request, 'Product update succcessfully')
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove items from shopping bag """
    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        messages.success(request, 'Product Delete succcessfully')
        return HttpResponse(status=200)

    except KeyError:
        return HttpResponse(status=500)
