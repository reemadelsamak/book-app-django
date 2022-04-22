from django.urls import path
from .views import index, get_single_book, get_author, create_book, update_book, delete_book
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Books
    path('books', index, name="index"),
    path('books/<int:book_ISBN>', get_single_book, name='get_book'),

    # Books CRUD
    path('books/create', create_book, name='create_book'),
    path('books/update/<int:book_ISBN>', update_book, name='update_book'),
    path('books/delete/<int:book_ISBN>', delete_book, name='delete_book'),

    # Authors
    path('books/author/<int:author_id>', get_author, name='get_author')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
