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
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="event_created_by",
        default=get_default_author,
        blank=True,
    )

    def __str__(self):
        """
        Returns the title of the event.
        """
        return self.title