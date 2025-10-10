from django.urls import path 

from .views import CustomTokenObtainView 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('custom', CustomTokenObtainView.as_view(), name='custom_token'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]