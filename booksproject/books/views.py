from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Book, Author
from .forms import Book_Form

# Create your views here.


def index(request):
    context = {"books": Book.objects.all()}
    return render(request, "books/index.html", context=context)


def get_single_book(request, book_ISBN):
    book = get_object_or_404(Book, ISBN=book_ISBN)
    context = {"book": book}
    return render(request, "books/book_details.html", context=context)


def get_author(request, author_id):
    books = Book.objects.filter(author_id=author_id).all()
    author = get_object_or_404(Author, id=author_id)
    context = {"author": author, "books": books}
    return render(request, "books/author.html", context=context)


def create_book(request):
    if request.method == "POST":
        form = Book_Form(request.POST, request.FILES)

        if form.is_valid():
            book = form.save()
            return redirect('index')
    else:
        form = Book_Form()
    return render(request, "books/book_create.html", context={'form': form})


def update_book(request, book_ISBN):
    book = get_object_or_404(Book, ISBN=book_ISBN)

    if request.method == "POST":
        form = Book_Form(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            context = {"book": book}
            return render(request, "books/book_details.html", context=context)
    else:
        form = Book_Form(instance=book)
    return render(request, "books/book_update.html", context={'form': form, 'book': book})


def delete_book(request, book_ISBN):
    book = get_object_or_404(Book, ISBN=book_ISBN)
    book.delete()

    return redirect('index')
