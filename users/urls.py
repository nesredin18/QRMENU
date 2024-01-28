from django.urls import path
from users import views


urlpatterns=[
    path('registeruser',views.RegisterAPIView.as_view(),name='register user'),
    path('login',views.LoginAPIView.as_view(),name='login user'),
    path('user',views.UserAPIView.as_view(),name='user'),
]