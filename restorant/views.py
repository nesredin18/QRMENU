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
    authentication_classes=[]

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer



class RestaurantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class UpdateRestaurantQRCodeAPIView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class UpdateRestaurantQRCodeAPIView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class UpdateRestaurantQRCodeAPIView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def update(self, request, *args, **kwargs):
        restaurant = self.get_object()
        url = request.data.get('url')

        if url:
            restaurant.url = url
            filename = f"restaurant_{restaurant.pk}_qr.png"

            # Generate a new QR code
            qr_code_file = generate_qr_code(url, filename)

            # Delete the existing file if it exists
            if restaurant.qr_code:
                restaurant.qr_code.delete(save=False)

            # Manually set the file path and save it
            file_path = os.path.join(settings.MEDIA_ROOT, 'restaurant_qr_codes', filename)
            with open(file_path, 'wb') as file:
                file.write(qr_code_file.read())

            # Update the FileField path
            restaurant.qr_code.name = os.path.join('restaurant_qr_codes', filename)
            restaurant.save()
            
            return Response({'message': 'QR Code updated successfully'}, status=status.HTTP_200_OK)

        return Response({'message': 'URL is required'}, status=status.HTTP_400_BAD_REQUEST)

class ListRestaurantsAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RetrieveRestaurantAPIView(generics.RetrieveAPIView):
    authentication_classes=[]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

