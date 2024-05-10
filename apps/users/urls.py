from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.users.views import UserAPI

router = DefaultRouter()
router.register('user', UserAPI, basename='api_user')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='api_login'),
    path('refresh/', TokenRefreshView.as_view(), name='api_refresh')
]

urlpatterns += router.urls