# Generated by Django 4.2 on 2024-09-05 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wishlist", "0004_wishlist_size"),
    ]

    operations = [
        migrations.AddField(
            model_name="wishlist",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=6, null=True
            ),
        ),
    ]