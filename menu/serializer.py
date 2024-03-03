from rest_framework import serializers
from .models import Menu
from .models import MenuItem, MenuItemImage

class MenuSerializer(serializers.ModelSerializer):
    restaurant_id = serializers.IntegerField(required=True)
    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'title', 'description', 'is_active', 'restaurant_id']
        read_only_fields = ['id', 'restaurant']


class MenuItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemImage
        fields = ['id', 'menu_item', 'image_url', 'description']
        

class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ['id', 'menu', 'name', 'description', 'price']

class RestaurantMenuItemSerializer(serializers.ModelSerializer):
    menu_name = serializers.SerializerMethodField()
    restaurant_name = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = ['id', 'menu', 'menu_name', 'name', 'restaurant_name', 'description', 'price', 'is_active']

    def get_menu_name(self, obj):
        return obj.menu.title if obj.menu else None

    def get_restaurant_name(self, obj):
        return obj.menu.restaurant.name if obj.menu and obj.menu.restaurant else None