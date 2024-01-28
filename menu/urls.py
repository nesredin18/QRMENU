from django.urls import path
from .views import MenuItemImageListCreateAPIView, MenuItemImageRetrieveUpdateDestroyAPIView, MenuListCreateAPIView, MenuRetrieveUpdateDestroyAPIView
from .views import MenuItemListCreateAPIView, MenuItemRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('menus/', MenuListCreateAPIView.as_view(), name='menu-list-create'),
    path('menus/<int:pk>/', MenuRetrieveUpdateDestroyAPIView.as_view(), name='menu-retrieve-update-delete'),
    path('menu-items/', MenuItemListCreateAPIView.as_view(), name='menu-item-list-create'),
    path('menu-items/<int:pk>/', MenuItemRetrieveUpdateDestroyAPIView.as_view(), name='menu-item-retrieve-update-delete'),
     path('menu-item-images/', MenuItemImageListCreateAPIView.as_view(), name='menu-item-image-list-create'),
    path('menu-item-images/<int:pk>/', MenuItemImageRetrieveUpdateDestroyAPIView.as_view(), name='menu-item-image-retrieve-update-delete')
]
