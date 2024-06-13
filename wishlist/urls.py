from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/', views.wishlist_list, name='wishlist_list'),
    path('wishlist/add/', views.wishlist_add, name='wishlist_add'),
    path('wishlist/edit/<int:id>/', views.wishlist_edit, name='wishlist_edit'),
    path('wishlist/delete/<int:id>/', views.wishlist_delete, name='wishlist_delete'),
]