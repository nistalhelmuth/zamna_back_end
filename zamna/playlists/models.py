from django.db import models
from books.models import Book
from django.contrib.auth.models import User


# Playlist
class Playlist(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    book_id = models.IntegerField()


# Rating
class Rating(models.Model):
    playlist_id = models.ForeignKey(Playlist, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


# Comment
class Comment(models.Model):
    book_id = models.IntegerField()
    playlist_id = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
