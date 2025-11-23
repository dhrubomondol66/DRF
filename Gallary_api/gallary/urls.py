from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlbumViewSet, PhotoViewSet, gallery_view, album_detail

router = DefaultRouter()
router.register('albums', AlbumViewSet)
router.register('photos', PhotoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', gallery_view, name='gallery'),
    path('album/<int:pk>/', album_detail, name='album_detail'),
]

