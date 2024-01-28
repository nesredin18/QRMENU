from django.urls import path
from .views import RestaurantListCreateAPIView, RestaurantRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('restaurants/', RestaurantListCreateAPIView.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantRetrieveUpdateDestroyAPIView.as_view(), name='restaurant-retrieve-update-delete')
]
