from django.db import models


# Book
class Book(models.Model):
    goodreads_id = models.CharField(max_length=255)
