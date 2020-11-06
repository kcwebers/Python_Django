from django.shortcuts import render, redirect
from .models import Show
from .models import *
from django.contrib import messages


def redir(request):
    return redirect("/shows")

def index(request):
    context = {
    	"all_shows": Show.objects.all(),
    }
    return render(request, "semi_restful_app/index.html", context)

def show(request, show_id):
    context = {
        "show_info": Show.objects.get(id=show_id),
        "release_date": Show.objects.get(id=show_id).release_date.strftime("%B %d, %Y")
    }
    return render(request, "semi_restful_app/show.html", context)

def new(request):
    return render(request, "semi_restful_app/new.html")

def create(request):
    errors = Show.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/shows/new")
    else:    
        show = Show.objects.create(
            title=request.POST['title'], 
            network=request.POST['network'], 
            release_date=request.POST['released'], 
            desc=request.POST['descript'])
        show_id = show.id

        return redirect("/shows/"+ str(show_id))

def edit(request, show_id):
        show_info = Show.objects.get(id=show_id)
        time_made = show_info.release_date.strftime("%Y-%m-%d")

        context = {
            "show_info": show_info,
            "date_released": time_made
        }
        return render(request, "semi_restful_app/edit.html", context)

def update(request, show_id):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 1:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/shows/"+ show_id + "/edit")
    else:
        updated_info = Show.objects.get(id=show_id)
        updated_info.title = request.POST['title']
        updated_info.network = request.POST['network']
        updated_info.release_date = request.POST['released']
        updated_info.desc = request.POST['descript']
        updated_info.save()
        return redirect("/shows")

def delete(request, show_id):
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect("/shows")
