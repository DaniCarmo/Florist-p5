# Generated by Django 4.2 on 2024-06-07 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0002_remove_event_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="created_on",
        ),
    ]
