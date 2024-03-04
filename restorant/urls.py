from django.urls import path
from .views import RestaurantListCreateAPIView
from .views import (UpdateRestaurantQRCodeAPIView,UpdateRestaurantAPIView )
urlpatterns = [
    path('add-restorant/', RestaurantListCreateAPIView.as_view(), name='restaurant-list-create'),
    path('update-restorant/<int:pk>/', UpdateRestaurantQRCodeAPIView.as_view(), name='update-restaurant-qr'),
    path('update-restaurant-details/<int:pk>/', UpdateRestaurantAPIView.as_view(), name='update-restaurant-details'),

]
