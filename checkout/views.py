from django.shortcuts import (render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Oops, looks like there's nothing in your bag")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51P6pkHKIKutPZoQKiNpVENzY04GNdfE8ino4nPbORVyomEi1pFG91QDA198Q1TKzFpaIYrErZ6X2lN7jqpTAZXuU00wfv6GeQl',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)