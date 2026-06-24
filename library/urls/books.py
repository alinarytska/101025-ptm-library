from library.views.books import BookListGenericView
from django.urls import path


urlpatterns = [
    path('', BookListGenericView.as_view())
]
