from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/', views.wishlist_list, name='wishlist_list'),
    path('wishlist/add/<int:product_id>/', views.wishlist_add, name='wishlist_add'),
    path('wishlist/edit/<int:product_id>/', views.wishlist_edit, name='wishlist_edit'),
    path('wishlist/delete/<int:product_id>/', views.wishlist_delete, name='wishlist_delete'),
]