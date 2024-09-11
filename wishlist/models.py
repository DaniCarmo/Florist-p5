from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                null=True, blank=True)

    def __str__(self):
        return self.id
