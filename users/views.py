from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from users.models import User
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from users.serializers import UserListSerializer, ChangePasswordSerializer



from users.serializers import LoginSerializer, ProfileSerializer, RegisterSerializer, RegisterSuperUserSerializer
from rest_framework import response,status,permissions
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

# Create your views here.
class RegisterSuperUserAPIView(GenericAPIView):
    permission_classes=[permissions.IsAuthenticated,]
    serializer_class=RegisterSuperUserSerializer

    def post(self,request):

        data = request.data.copy()

        # Set the username to be the same as the email
        data['username'] = data['email']
        data['password'] = make_password(data['password'])
        data['is_staff'] = True
        data['is_superuser'] = True
        serializers=self.serializer_class(data=data)


        if serializers.is_valid():
            serializers.save()
            return response.Response(serializers.data,status=status.HTTP_201_CREATED)
        
        return response.Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class RegisterAPIView(GenericAPIView):
    authentication_classes=[]
    serializer_class=RegisterSerializer

    def post(self,request):

        data = request.data.copy()

        # Set the username to be the same as the email
        data['username'] = data['email']
        serializers=self.serializer_class(data=data)


        if serializers.is_valid():
            serializers.save()
            return response.Response(serializers.data,status=status.HTTP_201_CREATED)
        
        return response.Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPIView(GenericAPIView):
    authentication_classes=[]
    serializer_class=LoginSerializer

    def post(self,request):
        e=request.data.get('email',None)
        p=request.data.get('password',None)

        user=authenticate(username=e,password=p)

        if user:
            serializer=self.serializer_class(user)
            return response.Response(serializer.data,status=status.HTTP_200_OK)
        
        return response.Response({'message':"invalide password"},status=status.HTTP_401_UNAUTHORIZED)


class UserAPIView(GenericAPIView):

    permission_classes=[permissions.IsAuthenticated,]

    def get(self,request):

        user=request.user 
        serializer=ProfileSerializer(user)
        return response.Response(serializer.data,status=status.HTTP_200_OK)
    
class NonSuperuserListAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Retrieve all users that are not superusers
        return User.objects.filter(is_superuser=False)
    
class UserActivationDeactivationAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user.is_active = not user.is_active
        user.save()

        serializer = UserListSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ChangePasswordAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        old_password = serializer.validated_data['old_password']
        new_password = serializer.validated_data['new_password']

        # Check if the old password is correct
        if not user.check_password(old_password):
            return Response({'detail': 'Old password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

        # Change the password
        user_manager = user.__class__.objects
        user_manager.change_password(user, new_password)

        return Response({'detail': 'Password changed successfully.'}, status=status.HTTP_200_OK)