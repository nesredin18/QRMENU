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

class MenuItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
class MenuUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'description', 'is_active']

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance
    
class RestaurantMenuItemSerializer(serializers.ModelSerializer):
    menu_name = serializers.SerializerMethodField()
    restaurant_name = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = ['id', 'menu', 'menu_name', 'name', 'restaurant_name', 'description', 'price', 'is_active', 'images']

    def get_menu_name(self, obj):
        return obj.menu.title if obj.menu else None

    def get_restaurant_name(self, obj):
        return obj.menu.restaurant.name if obj.menu and obj.menu.restaurant else None

    def get_images(self, obj):
        menu_item_images = MenuItemImage.objects.filter(menu_item=obj)
        return [{'image_id': image.id, 'image_url': str(image.image_url), 'description': image.description} for image in menu_item_images]