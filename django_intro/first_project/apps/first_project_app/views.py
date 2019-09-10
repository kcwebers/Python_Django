from django.shortcuts import render, HttpResponse, redirect
from .models import Movie

def index(request):
    context = {
    	"all_the_movies": Movie.objects.all()
    }
    return render(request, "first_project_app/index.html", context)

def new(request):
    return HttpResponse("to later display a list of all blogs")

def create(request):
    return redirect("/")

def show(request, id):
    return HttpResponse("placeholder to display blog number: " + str(id))

def edit(request, id):
    return HttpResponse("placeholder to edit blog number: " + str(id))

def destroy(request, id):
    return redirect("/")