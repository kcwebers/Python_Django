from django.shortcuts import render, HttpResponse
from time import gmtime, strftime


def index(request):
    context = {
        "time": strftime("%B %d, %Y %H:%M %p", gmtime())
    }
    return render(request,'app_name/index.html', context)
