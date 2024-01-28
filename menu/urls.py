from django.urls import path
from .views import MenuItemImageListCreateAPIView, MenuItemImageRetrieveUpdateDestroyAPIView, MenuItemImagesByMenuItemAPIView, MenuItemsByMenuAPIView, MenuListCreateAPIView, MenuRetrieveUpdateDestroyAPIView, MenusByRestaurantAPIView
from .views import MenuItemListCreateAPIView, MenuItemRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('menus/', MenuListCreateAPIView.as_view(), name='menu-list-create'),
    path('menus/<int:pk>/', MenuRetrieveUpdateDestroyAPIView.as_view(), name='menu-retrieve-update-delete'),
    path('menu-items/', MenuItemListCreateAPIView.as_view(), name='menu-item-list-create'),
    path('menu-items/<int:pk>/', MenuItemRetrieveUpdateDestroyAPIView.as_view(), name='menu-item-retrieve-update-delete'),
    path('menu-item-images/', MenuItemImageListCreateAPIView.as_view(), name='menu-item-image-list-create'),
    path('menu-item-images/<int:pk>/', MenuItemImageRetrieveUpdateDestroyAPIView.as_view(), name='menu-item-image-retrieve-update-delete'),
    path('restaurants/<int:restaurant_id>/menus/', MenusByRestaurantAPIView.as_view(), name='menus-by-restaurant'),
    path('menus/<int:menu_id>/menu-items/', MenuItemsByMenuAPIView.as_view(), name='menu-items-by-menu'),
    path('menu-items/<int:menu_item_id>/images/', MenuItemImagesByMenuItemAPIView.as_view(), name='menu-item-images-by-menu-item'),
]


