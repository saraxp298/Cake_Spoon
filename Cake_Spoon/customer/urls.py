from django import views
from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.login,name='loginpage'),
    path('register/',views.register,name='register')
    
]