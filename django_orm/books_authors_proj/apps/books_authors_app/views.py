from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    context = {
    	"all_books": Book.objects.all(),
    }
    return render(request, "books_authors_app/index.html", context)

def add_title(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])

    return redirect("/")

def attribute_title(request):
    this_auth = Author.objects.get(id=request.POST['auth_id'])

    this_auth.books.add(Book.objects.get(id=request.POST['book_id']))
    return redirect("/authors/"+request.POST['auth_id'])

def authors(request):
    context = {
    	"all_authors": Author.objects.all()
    }
    return render(request, "books_authors_app/authors.html", context)

def add_author(request):
    Author.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'],notes=request.POST['notes'])
    return redirect("/authors")

def attribute_author(request):
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_book.authors.add(Author.objects.get(id=request.POST['auth_id']))
    return redirect("/books/"+request.POST['book_id'])

def book_info(request, book_id):
    context = {
        "book" : Book.objects.get(id=book_id),
        "authors" : Book.objects.get(id=book_id).authors.all(),
        "all_authors" : Author.objects.all()
    }
    return render(request, "books_authors_app/book_info.html", context)

def author_info(request, auth_id):
    context = {
        "author" : Author.objects.get(id=auth_id),
        "books" : Author.objects.get(id=auth_id).books.all(),
        "all_books" : Book.objects.all()
    }
    return render(request, "books_authors_app/author_info.html", context)
