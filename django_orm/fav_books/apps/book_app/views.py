from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'book_app/index.html')

def success_reg(request):
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect("/")
        else: # no errors then this
            user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode())

            request.session['first_name'] = request.POST['first_name']
            request.session['id'] = user.id
            return redirect('/books')

def success_log(request):
    if request.method == "POST":
        errors = User.objects.log_validator(request.POST)
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        if len(errors) > 0:
            return redirect("/")
        else: # no errors than this 

            user_email = request.POST['email_input']
            user = User.objects.get(email=user_email)
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['id'] = user.id

            return redirect('/books')

def books(request):
    if not 'first_name' in request.session:
        errors = User.objects.not_logged(request.POST)
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")
    elif not 'last_name' in request.session:
        errors = User.objects.success_login_validation(request.POST)
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            context = {
                "all_books": Book.objects.all()
            }

            return render(request, "book_app/books.html", context)
    else: 
        errors = User.objects.success_reg_validation(request.POST)
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            context = {
                "all_books": Book.objects.all(), # pulls the entire book class, need to loop through to access sub
                "user": User.objects.get(id=request.session['id'])
            }
            return render(request, "book_app/books.html", context)

def logout(request):
    request.session.clear()
    return redirect('/')

def add_book(request):
    if request.method == "POST":
        errors = Book.objects.book_validator(request.POST)
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            return redirect('/books')
        if len(errors) > 0:
            return redirect("/")
        else:
            this_adder=User.objects.get(id=request.session['id'])
            new_book = Book.objects.create(
                title=request.POST['title'],
                desc=request.POST['desc'], 
                uploaded_by=this_adder
            )
            # adds user as the book's uploader
            new_book.users_who_like.add(this_adder) # when book added, user automatically favorites

        return redirect('/books')

def update_book(request):
    if request.method == "POST":
        errors = Book.objects.book_validator(request.POST)
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            return redirect('/books')
        if len(errors) > 0:
            return redirect("/")
        else:
            this_book = Book.objects.get(id=request.POST['book_id'])
            this_book.title = request.POST['title']
            this_book.desc = request.POST['desc']
            this_book.save
            return redirect('/books')

def delete(request, book_id):
    this_book = Book.objects.get(id=book_id)
    this_book.delete()

    return redirect("/books")

def show(request, book_id):
    this_book = Book.objects.get(id=book_id)
    if this_book.uploaded_by.id == request.session['id']:
        context = {
            "user": User.objects.get(id=request.session['id']),
            "this_book": this_book,
            "favorites": this_book.users_who_like.all()
        }
        return render(request, "book_app/edit_book.html", context)
    else:
        context = {
            "user": User.objects.get(id=request.session['id']),
            "this_book": this_book,
            "favorites": this_book.users_who_like.all()
        }
        return render(request, "book_app/show.html", context)

def favorite(request, book_id):
    this_book = Book.objects.get(id=book_id)
    this_user = User.objects.get(id=request.session['id'])
    if this_user in this_book.users_who_like.all():
        return redirect('/books')
    else:
        this_book.users_who_like.add(this_user)
        return redirect('/books/'+ str(book_id))

def unfavorite(request, book_id):
    this_book = Book.objects.get(id=book_id)
    this_user = User.objects.get(id=request.session['id'])
    
    this_book.users_who_like.remove(this_user)
    return redirect('/books/' + str(book_id))


    