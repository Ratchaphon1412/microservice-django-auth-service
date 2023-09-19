from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import *

urlpatterns = [
    path('user/login/',  LoginAPIView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/register/', RegisterUserAPI.as_view(), name='register'),
    path('user/update/', UpdateUserAPI.as_view(), name='update'),
    path('user/delete/', DeleteUserAPI.as_view(), name='delete'),
    path('user/verify/<uidb64>/<token>/', ActivateUserAPI.as_view(), name='verify'),
    path('user/re-verify', ReSendEmailVerify.as_view(), name='re-verify'),
    path('user/', GetUserAPI.as_view(), name='user'),
    
    path('user/address/', AddressAPI.as_view(), name='address'),
]