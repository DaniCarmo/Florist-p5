from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_review, name='submit_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('all/', views.all_reviews, name='all_reviews'),
    path('search/', views.search_results, name='search_results'),
]
