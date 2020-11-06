from django.shortcuts import render, HttpResponse, redirect


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