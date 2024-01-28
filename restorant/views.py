from rest_framework import generics
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework import permissions

class RestaurantListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer



class RestaurantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
