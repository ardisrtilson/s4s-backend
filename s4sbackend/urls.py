from django.conf.urls import include
from django.urls import path
from s4sbackendapi.views import register_user, login_user
from rest_framework import routers

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
