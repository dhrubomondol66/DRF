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

    def get_queryset(self):
        queryset = Photo.objects.all()
        album_id = self.request.query_params.get('album', None)
        if album_id is not None:
            queryset = queryset.filter(album_id=album_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

def gallery_view(request):
    return render(request, 'gallary.html')

def album_detail(request, pk):
    return render(request, 'album_detail.html')
