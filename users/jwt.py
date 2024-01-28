from django.conf import settings
from rest_framework.authentication import get_authorization_header, BaseAuthentication
import jwt
from rest_framework import exceptions

from users.models import User
class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):

        auth_header=get_authorization_header(request)
        auth_data=auth_header.decode('utf-8')
        auth_token=auth_data.split(" ")

        if len(auth_token)!=2:
            raise exceptions.AuthenticationFailed("invalide token")
        token=auth_token[1]

        try:
            payload=jwt.decode(token,settings.SECRET_KEY,algorithms="HS256")
            username=payload['username']
            user=User.objects.get(username=username)
            return (user,token)
        except jwt.ExpiredSignatureError as ex:
            raise exceptions.AuthenticationFailed("token has expired")
        except jwt.DecodeError as ex:
            raise exceptions.AuthenticationFailed("token is not valid")
        except User.DoesNotExist as no_user:
            raise exceptions.AuthenticationFailed("no such user")
        