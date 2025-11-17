from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, PhotoViewSet

router = DefaultRouter()
router.register('albums', AlbumViewSet)
router.register('photos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

