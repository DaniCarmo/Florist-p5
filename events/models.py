from django.db import models
from django.contrib.auth.models import User


def get_default_author():
    """
    Retrieves the default author for the Event model.
    """
    return User.objects.first()


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        """
        Returns the title of the event.
        """
        return self.title