from rest_framework import viewsets, status
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models, serializers


class PlaylistModelViewSet(viewsets.ModelViewSet):
    queryset = models.Playlist.objects.all()
    serializer_class = serializers.PlaylistSerializer

    @action(methods=['GET'], detail=False, url_path='book')
    def getAllPlaylistOfBook(self, request, pk=None):
        book_id = self.request.query_params['book_id']

        playlists = models.Playlist.objects.filter(book_id=book_id)
        playlists_serialize = serializers.PlaylistSerializer(playlists, many=True)

        return Response(playlists_serialize.data)

class RatingModelViewSet(viewsets.ModelViewSet):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer

    @action(methods=['GET'], detail=False, url_path='book')
    def getAllRatingsOfPLaylistsOfABook(self, request, pk=None):
        book_id = self.request.query_params['book_id']

        ratings = models.Rating.objects.filter(playlist_id__book_id=book_id)
        ratings_serialize = serializers.RatingSerializer(ratings, many=True)

        return Response(ratings_serialize.data)


class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

