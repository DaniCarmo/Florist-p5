from django import forms
from .models import Wishlist
from products.models import Product


class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['product']
