from django.urls import path

from .views import MainPageView

app_name = "store"

urlpatterns = [
    path("", MainPageView.as_view(), name="mainpage"),
    # path("books/", views.BookListView.as_view(), name="books"),
    # path("book/<int:pk>", views.BookDetailView.as_view(), name="book-detail"),
]
