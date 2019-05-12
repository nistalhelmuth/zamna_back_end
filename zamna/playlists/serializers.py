from rest_framework import serializers
from . import models


class PlaylistSerializer(serializers.ModelSerializer):
    #user = UserSerializar()
    class Meta:
        model = models.Playlist
        exclude = []


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating
        exclude = []


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        exclude = []

