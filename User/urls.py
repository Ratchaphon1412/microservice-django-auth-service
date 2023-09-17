from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import *

urlpatterns = [
    path('user/login/',  LoginAPIView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/register/', RegisterUserAPI.as_view(), name='register'),
    path('user/update/', UpdateUserAPI.as_view(), name='update'),
    path('user/delete/', DeleteUserAPI.as_view(), name='delete'),
    path('user/', GetUserAPI.as_view(), name='user'),
]