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

class UpdateRestaurantAPIView(generics.RetrieveUpdateAPIView):
    authentication_classes = []
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        # You can perform any additional logic here before saving the update
        serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)




