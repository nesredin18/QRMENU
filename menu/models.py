from django.db import models
from helpers.models import CommenModel
from django.utils.text import slugify
import os

from restorant.models import Restaurant

def menu_item_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/restaurant_<restaurant_name>/menuitem_<menu_item_name>/<filename>
    restaurant_name = slugify(instance.menu_item.menu.restaurant.name)
    menu_name=slugify(instance.menu_item.menu.title)
    menu_item_name = slugify(instance.menu_item.name)
    return f'restaurant_{restaurant_name}/menu_{menu_name}/menuitem_{menu_item_name}/{filename}'

# Create your models here.
class Menu(CommenModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.title

class MenuItem(CommenModel):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Handling multiple images via a related model
    # Image URLs will be stored in MenuItemImage model

    def __str__(self):
        return self.name

class MenuItemImage(CommenModel):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='images')
    image_url = models.ImageField(upload_to=menu_item_image_directory_path)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.image_url