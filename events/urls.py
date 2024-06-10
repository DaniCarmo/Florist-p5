from django.urls import path
from .views import add_event, delete_event, edit_event
from . import views

urlpatterns = [
    path("", views.event_list, name="events"),
    path("add/", views.add_event, name="add_event"),
    path("delete/<int:event_id>", views.delete_event, name="delete_event"),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
]