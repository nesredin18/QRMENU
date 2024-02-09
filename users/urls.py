from django.urls import path
from users import views


urlpatterns=[
    path('register-super-user',views.RegisterSuperUserAPIView.as_view(),name='register user'),
    path('register-user',views.RegisterAPIView.as_view(),name='register user'),
    path('login',views.LoginAPIView.as_view(),name='login user'),
    path('profile',views.UserAPIView.as_view(),name='user'),
]