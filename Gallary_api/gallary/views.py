from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Album, Photo
from .serializers import AlbumSerializer, PhotoSerializer
from .permissions import IsOwnerReadOnly
# Create your views here.

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes =[permissions.IsAuthenticated, IsOwnerReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
