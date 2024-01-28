from django.urls import path
from .views import RestaurantListCreateAPIView, RestaurantRetrieveUpdateDestroyAPIView
from .views import (UpdateRestaurantQRCodeAPIView, ListRestaurantsAPIView, RetrieveRestaurantAPIView)
urlpatterns = [
    path('restaurants/', RestaurantListCreateAPIView.as_view(), name='restaurant-list-create'),
   path('restaurants/update-qr/<int:pk>/', UpdateRestaurantQRCodeAPIView.as_view(), name='update-restaurant-qr'),
    path('restaurants/', ListRestaurantsAPIView.as_view(), name='list-restaurants'),
    path('restaurants/<int:pk>/', RetrieveRestaurantAPIView.as_view(), name='retrieve-restaurant'),
    path('restaurants/<int:pk>/', RestaurantRetrieveUpdateDestroyAPIView.as_view(), name='restaurant-retrieve-update-delete')
]
