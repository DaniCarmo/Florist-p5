from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'date',
        'time',
        'location',
    )

    ordering = ('id',)


admin.site.register(Event)
