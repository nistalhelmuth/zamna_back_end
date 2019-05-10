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
    def goodreads_books(self, request, pk=None):
        name = self.request.query_params['name']
        response = client.search_book(q=name)
        books = []
        print(response['results']['work'])
        print(len(response['results']['work']))
        for r in response['results']['work']:
            book = {
                'average_rating': r['average_rating'],
                'original_publication_year': r['original_publication_year']['#text'],
                'id': r['best_book']['id']['#text'],
                'title': r['best_book']['title'],
                'author': r['best_book']['author']['name'],
                'img': r['best_book']['image_url'],
                'small_img': r['best_book']['small_image_url'],
            }
            books.append(book)
        return Response(
            list(books)
        )

    @action(methods=['GET'], detail=False, url_path='book')
    def goodreads_book(self, request, pk=None):
        id = self.request.query_params['id']
        response = client.Book.show(id)
        return Response(
            response
        )


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

