from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LostItemViewSet, FoundItemViewSet

router = DefaultRouter()
router.register(r'lost-items', LostItemViewSet, basename='lost-items')
router.register(r'found-items', FoundItemViewSet, basename='found-items')

urlpatterns = [
    path('', include(router.urls)),
]


