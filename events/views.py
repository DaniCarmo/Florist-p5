from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm


def event_list(request):
    """
    A view to return all events
    """
    events = Event.objects.all()

    return render(request, "events/events.html", {"events": events})


@login_required
def add_event(request):
    """
    Allows admin to add event
    """
    if request.method == "POST":
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            messages.success(request, "Event has been added successfully!")
            return redirect("events")
        else:
            messages.error(request, "Failed to add event."
                           "Please ensure the form is valid.")
    else:
        event_form = EventForm()

    context = {
        "event_form": event_form,
    }
    return render(request, "events/add_event.html", {"event_form": event_form})


@login_required
def delete_event(request, event_id):
    """
    Allows admin to delete event
    """
    if not request.user.is_superuser:
        messages.error(request, 'Oops! Admins only.')
        return redirect(reverse('events'))

    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        event.delete()
        messages.success(request, 'Event deleted!')
        return redirect(reverse('events'))
    else:
        messages.error(request, 'Invalid request method.')
        return redirect(reverse("events"))


@login_required
def edit_event(request, event_id):
    """
    Allows admin to edit event
    """
    if not request.user.is_superuser:
        messages.error(request, 'Oops! Admins only.')
        return redirect(reverse('events'))

    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        event_form = EventForm(data=request.POST, instance=event)
        if event_form.is_valid():
            event_form.save()
            messages.success(request, 'Event updated!')
            return redirect(reverse('events'))
        else:
            messages.error(request, 'Please ensure form is valid.')
    else:
        event_form = EventForm(instance=event)

    template = 'events/edit_event.html'
    context = {
        'event_form': event_form,
        'event': event,
    }
    return render(request, template, context)
