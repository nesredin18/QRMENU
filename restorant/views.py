from django.conf import settings
import qrcode
from rest_framework import generics
import os
from helpers.utils import generate_qr_code
from .models import Restaurant
from .serializers import RestaurantSerializer
from rest_framework import permissions
from rest_framework import generics, status
from rest_framework.response import Response
from django.core.files.storage import default_storage


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
    authentication_classes = []
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class UpdateRestaurantQRCodeAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer



