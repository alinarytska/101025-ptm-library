from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from library.views.borrows import BorrowViewSet
from library.views.event import EventViewSet
from library.views.libraries import LibraryViewSet
from library.views.posts import PostViewSet
from library.views.users import UserViewSet
from library.views.authors import AuthorViewSet


default_router = DefaultRouter()
default_router.register('posts', PostViewSet, basename='posts')
default_router.register('events', EventViewSet, basename='events')
default_router.register('authors', AuthorViewSet, basename='authors')
default_router.register('users', UserViewSet, basename='users')
default_router.register('borrows', BorrowViewSet, basename='borrows')
default_router.register('libraries', LibraryViewSet, basename='libraries')
default_router.register('categories', LibraryViewSet, basename='categories')


urlpatterns = [
    path('auth-jwt/', TokenObtainPairView.as_view()),
    path('refresh-jwt/', TokenRefreshView.as_view()),
    path('books/', include('library.urls.books')),
]

urlpatterns += default_router.urls
