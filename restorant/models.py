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
    qr_code = models.ImageField(upload_to=restaurant_image_directory_path, blank=True)
    url = models.URLField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        # Check if the object is new
        is_new = self._state.adding 

        if is_new:
            super().save(*args, **kwargs)  # Save first to get an ID

            # Update URL
            self.url = f"{settings.SITE_URL}/restaurants/{self.name}/menus/"
            
            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(self.url)
            qr.make(fit=True)

            qr_img = qr.make_image(fill='black', back_color='white')
            canvas = Image.new('RGB', (qr_img.pixel_size, qr_img.pixel_size), 'white')
            draw = ImageDraw.Draw(canvas)
            canvas.paste(qr_img)

            # Save QR code to BytesIO
            buffer = BytesIO()
            canvas.save(buffer, format='PNG')
            buffer.seek(0)

            # Save image to qr_code field
            self.qr_code.save(f"restaurant_{self.name}_qr.png", File(buffer), save=False)

        if not is_new:
            super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    
class QRCode(CommenModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='qrcodes')
    url = models.URLField()
    generated_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.url