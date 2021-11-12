from django.contrib import admin
from django.urls import path
from .views import RegisterAPI,LoginAPI,UserAPI,ChangePasswordAPI


urlpatterns = [

    path('api/register/',RegisterAPI.as_view(),name='register'),
    path('api/login/',LoginAPI.as_view(),name='login'),
    path('api/user/',UserAPI.as_view(),name='user'),
    path('api/changepwd/',ChangePasswordAPI.as_view(),name='changepwd')
]
