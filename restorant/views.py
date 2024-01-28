from django.conf import settings
import qrcode
from rest_framework import generics
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework import permissions


def generate_qr_code_for_restaurant(restaurant_id):
    url = f"{settings.SITE_URL}/restaurants/{restaurant_id}/menus/"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_path = f"media/qr_codes/restaurant_{restaurant_id}.png"
    img.save(img_path)

    return img_path

class RestaurantListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer



class RestaurantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
