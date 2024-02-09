from rest_framework import generics

from restorant.models import Restaurant
from .models import Menu, MenuItemImage
from .serializer import MenuItemImageSerializer, MenuSerializer
from .models import MenuItem
from .serializer import MenuItemSerializer
from rest_framework.exceptions import NotFound

class MenuListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes=[]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[]

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuItemListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes=[]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemImageListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes=[]
    queryset = MenuItemImage.objects.all()
    serializer_class = MenuItemImageSerializer

class MenuItemImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[]
    queryset = MenuItemImage.objects.all()
    serializer_class = MenuItemImageSerializer

class MenusByRestaurantAPIView(generics.ListAPIView):
    authentication_classes=[]
    serializer_class = MenuSerializer
    authentication_classes=[]

    def get_queryset(self):

        restaurant_id = self.kwargs.get('id')
        if not Restaurant.objects.filter(id=restaurant_id).exists():
            raise NotFound(f"Restaurant with id {restaurant_id} not found.")
        
        return Menu.objects.filter(restaurant_id=restaurant_id)

class MenuItemsByMenuAPIView(generics.ListAPIView):
    authentication_classes=[]
    serializer_class = MenuItemSerializer

    def get_queryset(self):

        menu_id = self.kwargs.get('id')
        if not Menu.objects.filter(id=menu_id).exists():
            raise NotFound(f"Menu with id {menu_id} not found.")
        
        return MenuItem.objects.filter(menu_id=menu_id)

class MenuItemImagesByMenuItemAPIView(generics.ListAPIView):
    authentication_classes=[]
    serializer_class = MenuItemImageSerializer

    def get_queryset(self):
        """
        This view returns a list of all the images for the menu item 
        as determined by the menu_item_id portion of the URL.
        """
        menu_item_id = self.kwargs.get('id')
        if not MenuItem.objects.filter(id=menu_item_id).exists():
            raise NotFound(f"MenuItem with id {menu_item_id} not found.")
        
        return MenuItemImage.objects.filter(menu_item_id=menu_item_id)
