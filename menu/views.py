from rest_framework import generics
from .models import Menu, MenuItemImage
from .serializer import MenuItemImageSerializer, MenuSerializer
from .models import MenuItem
from .serializer import MenuItemSerializer

class MenuListCreateAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = MenuItemImage.objects.all()
    serializer_class = MenuItemImageSerializer

class MenuItemImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItemImage.objects.all()
    serializer_class = MenuItemImageSerializer
