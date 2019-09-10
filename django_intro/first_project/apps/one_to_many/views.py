from django.shortcuts import render
from .models import Author, Book

def index(request):
    context = {
        "authors": Author.objects.all()
    }		# we're only sending up all the authors
    return render(request, "one_to_many/index.html", context)

