from rest_framework import serializers
from restorant.models import Restaurant

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
            try:
                restaurant = Restaurant.objects.get(id=restaurant_id)
                restaurant.owner = user
                restaurant.save()
            except Restaurant.DoesNotExist:
                pass  # or handle as you see fit

        return user
    
class LoginSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=120,min_length=6,write_only=True,required=True)

    class Meta():
        model=User
        fields=['password','email','token',]
        read_only_fields=['token']
