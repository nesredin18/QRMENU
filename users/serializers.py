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
    restaurant_id = serializers.IntegerField(write_only=True, required=True)
    first_name = serializers.CharField(max_length=30, required=True)
    last_name = serializers.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'restaurant_id', 'mobile', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        restaurant_id = validated_data.pop('restaurant_id', None)
        first_name = validated_data.pop('first_name', None)
        last_name = validated_data.pop('last_name', None)

        # Create the user with the validated data
        user = User.objects.create_user(**validated_data)

        # Set additional fields (first_name and last_name)
        user.first_name = first_name
        user.last_name = last_name

        if restaurant_id:
            with transaction.atomic():
                try:
                    restaurant = Restaurant.objects.get(id=restaurant_id)
                    user.restaurant = restaurant
                    user.save()
                except Restaurant.DoesNotExist:
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

class ProfileSerializer(serializers.ModelSerializer):
    restaurant_id = serializers.SerializerMethodField()
    restaurant_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile', 'restaurant_id', 'restaurant_name', 'is_staff', 'is_superuser', 'is_active', 'first_name', 'last_name']
        read_only_fields = ['id', 'username', 'email', 'restaurant_id', 'restaurant_name']

    def get_restaurant_id(self, obj):
        return obj.restaurant.id if obj.restaurant else None

    def get_restaurant_name(self, obj):
        return obj.restaurant.name if obj.restaurant else None

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile', 'restaurant_id', 'is_staff', 'is_superuser', 'is_active', 'first_name', 'last_name']

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)