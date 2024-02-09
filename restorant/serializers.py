from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id',  'name', 'address', 'contact_info', 'logo_url', 'qr_code', 'url']
        read_only_fields = ['id']

