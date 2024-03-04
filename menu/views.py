from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes, renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from restorant.models import Restaurant
from .models import Menu, MenuItemImage
from .serializer import MenuItemImageSerializer, MenuSerializer, RestaurantMenuItemSerializer
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

class MenuItemsByRestaurantAPIView(generics.ListAPIView):
    authentication_classes = []
    serializer_class = RestaurantMenuItemSerializer  

    def get_queryset(self):
        restaurant_id = self.kwargs.get('id')
        if not Restaurant.objects.filter(id=restaurant_id).exists():
            raise NotFound(f"Restaurant with id {restaurant_id} not found.")

        return MenuItem.objects.filter(menu__restaurant_id=restaurant_id)
    
@api_view(['GET', 'POST'])
def menu_item_image_list_create_view(request):
    """
    List all menu item images or create a new one.
    """
    if request.method == 'GET':
        menu_item_images = MenuItemImage.objects.all()
        serializer = MenuItemImageSerializer(menu_item_images, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MenuItemImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@authentication_classes([])  
@permission_classes([AllowAny])  
@renderer_classes([JSONRenderer]) 
def restaurant_menu_and_items(request, restaurant_id):
    try:
        menus = Menu.objects.filter(restaurant_id=restaurant_id)
        restaurant_name = menus.first().restaurant.name  
        restaurant_id = menus.first().restaurant.id

        result = {
            'restaurantName': restaurant_name,
            'restaurantId': restaurant_id,
            'menus': [],
        }

        for menu in menus:
            menu_data = {
                'menuTitle': menu.title,
                'menuDescription': menu.description,
                'menuIsActive': menu.is_active,
                'menuItems': [],
            }

            menu_items = MenuItem.objects.filter(menu=menu)
            for menu_item in menu_items:
                menu_item_data = {
                    'menuItemId': menu_item.id,
                    'name': menu_item.name,
                    'menuId': menu_item.menu.id,
                    'description': menu_item.description,
                    'price': menu_item.price,
                    'images': [],
                }

                menu_item_images = MenuItemImage.objects.filter(menu_item=menu_item)
                for menu_item_image in menu_item_images:
                    menu_item_data['images'].append({
                        'imageId': menu_item_image.id,
                        'imageUrl': str(menu_item_image.image_url),
                        'description': menu_item_image.description,
                    })

                menu_data['menuItems'].append(menu_item_data)

            result['menus'].append(menu_data)

        return Response(result, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)