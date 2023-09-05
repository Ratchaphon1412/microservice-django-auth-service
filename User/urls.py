from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import RegisterAPI

urlpatterns = [
    path('user/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/register/', RegisterAPI.as_view(), name='register'),
]