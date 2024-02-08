from rest_framework import serializers
from restorant.models import Restaurant
from django.db import transaction
from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    restaurant_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'restaurant_id']
        extra_kwargs = {
            'password': {'write_only': True},
        }

def create(self, validated_data):
    restaurant_id = validated_data.pop('restaurant_id', None)
    user = User.objects.create_user(**validated_data)

    if restaurant_id:
        with transaction.atomic():
            try:
                restaurant = Restaurant.objects.get(id=restaurant_id)
                # Create the user profile linked to the restaurant
                User.objects.create(user=user, restaurant=restaurant)
            except Restaurant.DoesNotExist:
                return Response({'message': 'Restaurant not found'}, status=status.HTTP_400_BAD_REQUEST)
                  # Handle as you see fit, maybe raise an error or log this situation

    return user
    
class LoginSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=120,min_length=6,write_only=True,required=True)

    class Meta():
        model=User
        fields=['password','email','token',]
        read_only_fields=['token']
