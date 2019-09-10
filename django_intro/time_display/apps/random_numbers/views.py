from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# def some_function(request):
#     request.session['name'] = request.POST['name']
#     request.session['counter'] = 100

def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0
    if 'count' in request.session:
        request.session['count'] += 1
    context = {
        "session": request.session['count'],
        "random_word": get_random_string(length=14)
    }
    return render(request, "random_numbers/index.html", context)

def clear(request):
    request.session.clear()
    return redirect("/random_word")
