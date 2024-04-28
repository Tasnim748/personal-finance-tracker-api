from django.urls import path
from .customAuthToken import CustomAuthToken

urlpatterns = [
    path('auth/', CustomAuthToken.as_view())
]