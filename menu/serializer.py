from rest_framework import serializers
from .models import Menu
from .models import MenuItem, MenuItemImage

class MenuSerializer(serializers.ModelSerializer):
    restaurant_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'title', 'description', 'is_active', 'restaurant_id']
        read_only_fields = ['id', 'restaurant']


class MenuItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemImage
        fields = ['id', 'menu_item', 'image_url', 'description']
        

class MenuItemSerializer(serializers.ModelSerializer):
    images = MenuItemImageSerializer(many=True, read_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'menu', 'name', 'description', 'price']