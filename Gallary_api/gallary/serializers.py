from rest_framework import serializers
from .models import Album, Photo

class AlbumSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Album
        fields = ['id', 'title', 'description', 'created_at', 'owner']


class PhotoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    album_title = serializers.ReadOnlyField(source='album.title')

    class Meta:
        model = Photo
        fields = ['id', 'album', 'album_title', 'image', 'caption', 'updated_at', 'owner']