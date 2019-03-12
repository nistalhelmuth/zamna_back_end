from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books import views as books_views
from playlists import views as playlists_views


# Router creation
router = DefaultRouter()

# Books
router.register(
    r'books',
    books_views.BooksModelViewSet
)

# User
router.register(
    r'user',
    books_views.UserModelViewSet
)

# Playlist
router.register(
    r'playlist',
    playlists_views.PlaylistModelViewSet
)

# Rating
router.register(
    r'rating',
    playlists_views.RatingModelViewSet
)

# Comment
router.register(
    r'comment',
    playlists_views.CommentModelViewSet
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]