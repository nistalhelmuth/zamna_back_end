from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models, serializers

import goodreads_api_client as gr
client = gr.Client(developer_key='FtV2JkeEaiobnja5s890Q')

class BooksModelViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    @action(methods=['GET'], detail=False, url_path='search')
    # /notebook/all-notes/ devuelve todas las NOTAS dentro de del cuaderno
    def goodreads(self, request, pk=None):
        name = self.request.query_params['name']
        book = client.search_book(q=name)
        return Response(
            book
        )


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

