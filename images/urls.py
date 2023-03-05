from django.urls import path, include
from rest_framework import routers
from .views import ImageViewSet, AccountTierViewSet

router = routers.DefaultRouter()
router.register(r'images', ImageViewSet)
router.register(r'account-tiers', AccountTierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]