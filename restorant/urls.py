from django.urls import path
from .views import RestaurantListCreateAPIView
from .views import (UpdateRestaurantQRCodeAPIView, )
urlpatterns = [
    path('add-restorant/', RestaurantListCreateAPIView.as_view(), name='restaurant-list-create'),
   path('update-restorant/<int:pk>/', UpdateRestaurantQRCodeAPIView.as_view(), name='update-restaurant-qr'),
]
