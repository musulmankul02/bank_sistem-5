from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.transfer.views import TransferAPI

router = DefaultRouter()
router.register('transfer', TransferAPI , "api_transfer")




urlpatterns = router.urls