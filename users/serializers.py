from rest_framework import serializers
from restorant.models import Restaurant
from django.db import transaction
from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User
class RegisterSuperUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email','mobile','is_staff','is_superuser']
        extra_kwargs = {
            'password': {'write_only': True},
        }
        def create(self, validated_data):
            # Use Django's built-in create_superuser method to handle superuser creation.
            # This method correctly sets is_staff and is_superuser flags along with handling the password.
            user = User.objects.create_superuser(**validated_data)
            return user

class RegisterSerializer(serializers.ModelSerializer):
    restaurant_id = serializers.IntegerField(write_only=True,required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'restaurant_id','mobile']
        extra_kwargs = {
            'password': {'write_only': True},
        }


    def create(self, validated_data):
        restaurant_id = validated_data.pop('restaurant_id', None)
        # Create the user with the validated data
        user = User.objects.create_user(**validated_data)

        if restaurant_id:
            with transaction.atomic():
                try:
                    restaurant = Restaurant.objects.get(id=restaurant_id)
                    user.restaurant = restaurant  # Correctly assign the restaurant to the user's restaurant field
                    user.save()  # Don't forget to save the user after assigning the restaurant
                except Restaurant.DoesNotExist:
                    # Proper way to handle exception in serializer
                    raise serializers.ValidationError({'restaurant_id': 'Restaurant not found'})

        return user
    
class LoginSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=120,min_length=6,write_only=True,required=True)

    class Meta():
        model=User
        fields=['password','email','token',]
        read_only_fields=['token']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta():
        model=User
        fields=['username','email','mobile','restaurant','is_staff','is_superuser']
        read_only_fields=['username','email','restaurant']
