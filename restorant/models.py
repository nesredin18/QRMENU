from django.db import models
from django.db import models
from django.conf import settings
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.utils.text import slugify


from helpers.models import CommenModel

def restaurant_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/restaurant_<restaurant_name>/menuitem_<menu_item_name>/<filename>
    restaurant_name = slugify(instance.name)
    return f'restaurant_{restaurant_name}/{filename}'


# Create your models here.
class Restaurant(CommenModel):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    contact_info = models.CharField(max_length=100, blank=True)
    logo_url = models.ImageField(upload_to=restaurant_image_directory_path,blank=True)
    url = models.URLField(max_length=200, blank=True)




    def __str__(self):
        return self.name
    
class QRCode(CommenModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='qrcodes')
    url = models.URLField()
    generated_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.url